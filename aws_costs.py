class awslambda:

    _MILLION_REQS = 1000000

    def __init__(self, MB_per_req=128, ms_per_req=100):

        self.mem = MB_per_req
        self.exec_time = ms_per_req

        # Improvement: this data could be requested via AWS Costs API:
        self.cost_per_million_reqs = .20
        self.cost_per_GB_s = 0.00001667

        self.free_tier = (self._MILLION_REQS, 400000)
        self.reset_free_tier_counters()

    def __del__(self):
        pass

    @property
    def mem(self):
        return self.__mem_per_req

    @mem.setter
    def mem(self, megabytes):
        # TO-DO:comprobar que se mete un valor válido para una AWS lambda
        self.__mem_per_req = megabytes

    @property
    def exec_time(self):
        return self.__exec_time

    @exec_time.setter
    def exec_time(self, miliseconds):
        self.__exec_time = miliseconds

    @property
    def free_tier(self):
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

    def __get_free_tier_discount(self, resources, remaining_resources):
        if remaining_resources > resources:
            ret = (0, remaining_resources-resources)
        else:
            ret = (resources-remaining_resources, 0)

        return ret

    def get_hourly_cost(self, date, reqs):
        if date.day == 1 and date.hour == 0:
            self.reset_free_tier_counters()

        (reqs, self.remaining_free_reqs) = \
            self.__get_free_tier_discount(reqs, self.remaining_free_reqs)

        compute_GB_s = reqs * self.mem/1024 * self.exec_time/1000

        (compute_GB_s, self.remaining_free_GB_s) = \
            self.__get_free_tier_discount(
                compute_GB_s, self.remaining_free_GB_s
            )
        return (reqs / self._MILLION_REQS) * self.cost_per_million_reqs + \
            compute_GB_s * self.cost_per_GB_s
