import json
import math


class EC2:

    def __init__(self, instance_type, MB_per_req=128):

        self._cost_per_hour, self._memory = \
            self._get_instance_data(instance_type)

        self.max_concurrent_requests = self._memory // int(MB_per_req)

    def __init__(self, instance_type, max_concurrent_requests):

        self._cost_per_hour, self.memory = \
            self._get_instance_data(instance_type)
        self.max_concurrent_requests = max_concurrent_requests

    def __del__(self):
        pass

    @property
    def _memory(self):
        return self.__memory

    @_memory.setter
    def _memory(self, megabytes):
        self.__memory = megabytes

    @property
    def max_concurrent_requests(self):
        return self.__max_concurrent_requests

    @max_concurrent_requests.setter
    def max_concurrent_requests(self, reqs):
        self.__max_concurrent_requests = reqs

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

    def get_instances(self, reqs):
        return math.ceil(reqs/self.max_concurrent_requests)

    def get_cost_per_second(self, reqs):
        return self.get_instances(reqs) * self._cost_per_hour / 3600

    def get_cost_per_minute(self, reqs):
        # we assume here a uniform distribution of requests
        cost = self.get_cost_per_second(reqs/60) * 60
        return cost

    def get_hourly_cost(self, reqs):
        # we assume here a uniform distribution of requests
        cost = self.get_cost_per_second(reqs/3600) * 3600
        return cost
