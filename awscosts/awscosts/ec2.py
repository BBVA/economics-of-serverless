import json
import math


class EC2:

    def __init__(self, instance_type, MB_per_req=128):

        (self._cost_per_hour, self._memory) = \
            self._get_instance_data(instance_type)

        self.max_requests = self._memory // int(MB_per_req)

    def __del__(self):
        pass

    @property
    def _memory(self):
        return self.__memory

    @_memory.setter
    def _memory(self, megabytes):
        self.__memory = megabytes

    @property
    def max_requests(self):
        return self.__max_requests

    @max_requests.setter
    def max_requests(self, reqs):
        self.__max_requests = reqs

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
        return (price, memory)

    def get_hourly_cost(self, reqs):
        # we assume here a uniform distribution of requests
        cost = self.get_cost_in_a_second(reqs/3600) * 3600
        return cost

    def get_cost_in_a_second(self, reqs):
        number_instances = math.ceil(reqs/self.max_requests)
        cost = number_instances * self._cost_per_hour / 3600
        return cost
