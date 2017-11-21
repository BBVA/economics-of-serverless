import json
import math


class EC2:

    def __init__(self, instance_type, MB_per_req=128):

        (self.cost_per_hour, self.memory) = \
            self.get_instance_data(instance_type)

        self.max_requests = self.memory // int(MB_per_req)

    def __del__(self):
        pass

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, megabytes):
        self.__memory = megabytes

    @property
    def max_requests(self):
        return self.__max_requests

    @max_requests.setter
    def max_requests(self, reqs):
        self.__max_requests = reqs

    @property
    def cost_per_hour(self):
        return self.__cost_per_hour

    @cost_per_hour.setter
    def cost_per_hour(self, dollars):
        self.__cost_per_hour = dollars

    @staticmethod
    def get_instance_data(name):
        resource_path = '/'.join(('awscosts', 'awscosts', 'ec2prices.json'))
        data = json.load(open(resource_path))
        price = float(data[name]['hourly_price'])
        memory = int(float(data[name]['memory']) * 1024)
        return (price, memory)

    def get_hourly_cost(self, reqs):
        number_instances = math.ceil(reqs/self.max_requests)
        cost = number_instances * self.cost_per_hour
        return cost
