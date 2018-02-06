# Copyright 2018 BBVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Lambda:
    """AWS Lambda price object, used to calculate costs.

    Args:
        MB_per_req (int): memory consumed for this lambda. If not among AWS' lambda
            flavors, the selected flavor will be the minimum to fit the
            function. Defaults to 128 MB.
        ms_per_req (int): time (in miliseconds) that the function needs to run.
            Defaults to 100ms.
        use_penalty (bool, optional): Flag to apply performance penalty
            based on the selected flavor. Defaults to `False`.
        use_free_tier (bool, optional): Flag to control whether to use AWS free
            tier each new month (or manually when calling `get_cost`). Defaults
            to `True`.
    """
    _MILLION_REQS = 1000000

    _LAMBDA_FLAVORS = (
        128, 192, 256, 320, 384, 448, 512, 576,
        640, 704, 768, 832, 896, 960, 1024, 1088,
        1152, 1216, 1280, 1344, 1408, 1472, 1536
    )

    _PENALTY_TABLE = dict(zip(_LAMBDA_FLAVORS, [
        16.6, 11.78, 8.19, 5.84, 4.75, 4.30, 3.87, 3.50,
        3.14, 2.81, 2.54, 2.33, 2.16, 2.02, 1.89, 1.79,
        1.68, 1.61, 1.54, 1.49, 1.45, 1.42, 1.40
    ]))

    def __init__(self, MB_per_req=128, ms_per_req=100, use_penalty=False,
                 use_free_tier=True):

        # Select the lambda flavor that fits the amount of MB_per_req
        self.mem = min(x for x in self._LAMBDA_FLAVORS if x >= MB_per_req)

        self.penalty = self._PENALTY_TABLE[self.mem]

        # Exec time is calculated using penalty values from empirical table:
        self.exec_time = ms_per_req*self.penalty if use_penalty else ms_per_req

        # Improvement: this data could be requested via AWS Costs API:
        self.cost_per_million_reqs = .20
        self.cost_per_GB_s = 0.00001667

        if use_free_tier:
            self.free_tier = (self._MILLION_REQS, 400000)
        else:
            self.free_tier = (0, 0)

        self.reset_free_tier_counters()

    def __del__(self):
        pass

    @property
    def penalty(self):
        return self.__penalty_factor

    @penalty.setter
    def penalty(self, penalty):
        self.__penalty_factor = penalty

    @property
    def mem(self):
        return self.__mem_per_req

    @mem.setter
    def mem(self, megabytes):
        # TO-DO:comprobar que se mete un valor válido para una AWS lambda
        self.__mem_per_req = int(megabytes)

    @property
    def exec_time(self):
        return self.__exec_time

    @exec_time.setter
    def exec_time(self, miliseconds):
        self.__exec_time = miliseconds

    @property
    def free_tier(self):
        """list of int: tuple with free reqs and GB-s for each tier."""
        return (self.__free_reqs, self.__free_compute_GB_s)

    @free_tier.setter
    def free_tier(self, reqs_GB_s):
        try:
            reqs, GB_s = reqs_GB_s
        except ValueError:
            raise ValueError("Expected iterable with reqs and GB_s values")
        else:
            self.__free_reqs = reqs
            self.__free_compute_GB_s = GB_s

    @property
    def remaining_free_reqs(self):
        return self.__remaining_free_reqs

    @remaining_free_reqs.setter
    def remaining_free_reqs(self, reqs):
        self.__remaining_free_reqs = reqs

    @property
    def remaining_free_GB_s(self):
        return self.__remaining_free_GB_s

    @remaining_free_GB_s.setter
    def remaining_free_GB_s(self, GB_s):
        self.__remaining_free_GB_s = GB_s

    @property
    def cost_per_million_reqs(self):
        return self.__cost_per_million_reqs

    @cost_per_million_reqs.setter
    def cost_per_million_reqs(self, dollars):
        self.__cost_per_million_reqs = dollars

    @property
    def cost_per_GB_s(self):
        return self.__cost_per_GB_s

    @cost_per_GB_s.setter
    def cost_per_GB_s(self, dollars):
        self.__cost_per_GB_s = dollars

    def reset_free_tier_counters(self):
        (reqs, GB_s) = self.free_tier
        self.remaining_free_reqs = reqs
        self.remaining_free_GB_s = GB_s

    @staticmethod
    def __get_free_tier_discount(resources, remaining_resources):
        """Given a tuple with a `resource` (reqs or GB-s), and the remaining
        (free) counter of that resource, it substracts the `resources`

        Note: One of the two returning params will be 0:
        - in the first case, there will still be free resources
        - in the second case, no free resources will be left.

        Args:
            resources (int): reqs or GB-s to be substracted
            remaining_resources (int): remaining free reqs or GB-s from the
                free tier

        Returns:
            {
                'resources' (int): resources with cost,
                'remaining_resources' (int): new remaining free resources
            }
        """
        if remaining_resources > resources:
            ret = (0, remaining_resources - resources)
        else:
            ret = (resources - remaining_resources, 0)

        return ret

    def get_cost(self, reqs, date=None, reset_free_tier=False):
        """Calculates the cost of the given requests.

        Args:
            reqs (int): number of requests to bill.
            date (:obj:`datetime.date`, optional): day of the requests. Related
                with free tier calculation (resets counter if midnight of the
                first day of month)
            reset_free_tier (bool, optional): flag to reset the free tier
                counter before calculate the costs.

        Returns:
            float: price (in original currency) to bill for the requests.

        """
        # Reset free tier counters if requested, or if 1st day of month
        if reset_free_tier:
            self.reset_free_tier_counters()
        elif date is not None:
            if date.day == 1 and date.hour == 0:
                self.reset_free_tier_counters()

        compute_GB_s = reqs * self.mem / 1024 * self.exec_time / 1000

        (reqs, self.remaining_free_reqs) = \
            self.__get_free_tier_discount(reqs, self.remaining_free_reqs)

        (compute_GB_s, self.remaining_free_GB_s) = \
            self.__get_free_tier_discount(
                compute_GB_s, self.remaining_free_GB_s
        )

        return (reqs / self._MILLION_REQS) * self.cost_per_million_reqs + \
            compute_GB_s * self.cost_per_GB_s
