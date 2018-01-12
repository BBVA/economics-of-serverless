import json
import math


class EC2:
    """AWS EC2 price object, used to calculate costs.

    Note:
        max_concurrent_reqs and MB_per_request are mutually exclusive.

    Args:
        instance_type (str): EC2 instance flavor (e.g. "t2.micro")
        max_concurrent_reqs (int): Maximum number of requests that this
            instance can process per second.
        MB_per_req (float): Size in Megabytes of a request.
        ms_per_req (float): Duration in ms of a request.
    """
    def __init__(self, instance_type, **kwargs):
        self._cost_per_hour, self._memory = \
            self._get_instance_data(instance_type)

        if 'max_concurrent_reqs' in kwargs:
            self.max_concurrent_reqs = kwargs['max_concurrent_reqs']
        elif 'MB_per_req' and 'ms_per_req' in kwargs:
            reqs_per_second = \
                float(kwargs['MB_per_req']) / float(kwargs['ms_per_req'])
            self.max_concurrent_reqs = \
                self._memory / reqs_per_second
        else:
            error_text = "Either max_concurrent_reqs, or \
                        (MB_per_request and ms_per_req) needs to be set."
            raise ValueError(error_text)

    def __del__(self):
        pass

    @property
    def _memory(self):
        return self.__memory

    @_memory.setter
    def _memory(self, megabytes):
        self.__memory = megabytes

    @property
    def max_concurrent_reqs(self):
        return self.__max_concurrent_reqs

    @max_concurrent_reqs.setter
    def max_concurrent_reqs(self, reqs):
        self.__max_concurrent_reqs = reqs

    @property
    def _cost_per_hour(self):
        return self.__cost_per_hour

    @_cost_per_hour.setter
    def _cost_per_hour(self, dollars):
        self.__cost_per_hour = dollars

    @staticmethod
    def _get_instance_data(name):
        resource_path = '/'.join(('awscosts', 'awscosts', 'ec2prices.json'))
        data = json.load(open(resource_path))
        price = float(data[name]['hourly_price'])
        memory = int(float(data[name]['memory']) * 1024)
        return price, memory

    def get_num_instances(self, reqs):
        return math.ceil(reqs/self.max_concurrent_reqs)

    def get_cost_and_num_instances(self, seconds, **kwargs):
        if 'reqs' in kwargs:
            num_instances = self.get_num_instances(float(kwargs['reqs']))
        else:
            num_instances = 1

        cost = num_instances * seconds * self._cost_per_hour / 3600
        return (cost, num_instances)

    def get_cost(self, seconds):
        (cost, _) = self.get_cost_and_num_instances(seconds)
        return cost

    def get_cost_per_second(self, reqs):
        return self.get_num_instances(reqs) * self._cost_per_hour / 3600

    def get_cost_per_minute(self, reqs):
        # we assume here a uniform distribution of requests
        cost = self.get_cost_per_second(reqs/60) * 60
        return cost

    def get_cost_per_hour(self, reqs):
        # we assume here a uniform distribution of requests
        cost = self.get_cost_per_second(reqs/3600) * 3600
        return cost
