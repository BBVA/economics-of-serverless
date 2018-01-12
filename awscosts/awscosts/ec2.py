import json
import math


class EC2:
    """AWS EC2 price object, used to calculate costs.

    Note:
        `max_reqs_per_second` and `MB_per_request` are mutually exclusive.
        `max_reqs_per_second` takes precedence over the other two.

    Args:
        instance_type (str): EC2 instance flavor (e.g. ``t2.micro``).
        **max_reqs_per_second (int, optional): Maximum number of requests that
            this instance can process per second.
        **MB_per_req (float, optional): Size in Megabytes of a request.
        **ms_per_req (int, optional): Duration in ms of a request.
    """
    def __init__(self, instance_type, **kwargs):
        self._cost_per_hour, self._memory = \
            self._get_instance_data(instance_type)

        if 'max_reqs_per_second' in kwargs:
            self.max_reqs_per_second = kwargs['max_reqs_per_second']
        elif 'MB_per_req' in kwargs and 'ms_per_req' in kwargs:

            req_size = float(kwargs['MB_per_req'])
            req_time = float(kwargs['ms_per_req']) / 1000

            self.max_reqs_per_second = (self._memory / req_size) / req_time

        else:
            error_text = "Either max_reqs_per_second, or \
                        (MB_per_request and ms_per_req) needs to be set."
            raise ValueError(error_text)

    def __del__(self):
        pass

    @property
    def _memory(self):
        """int: EC2 instance RAM (Megabytes)"""
        return self.__memory

    @_memory.setter
    def _memory(self, megabytes):
        self.__memory = megabytes

    @property
    def max_reqs_per_second(self):
        return self.__max_reqs_per_second

    @max_reqs_per_second.setter
    def max_reqs_per_second(self, reqs):
        self.__max_reqs_per_second = reqs

    @property
    def _cost_per_hour(self):
        return self.__cost_per_hour

    @property
    def _cost_per_second(self):
        return self.__cost_per_second

    @_cost_per_hour.setter
    def _cost_per_hour(self, dollars):
        self.__cost_per_hour = dollars
        self.__cost_per_second = dollars / 3600

    @staticmethod
    def _get_instance_data(name):
        resource_path = '/'.join(('awscosts', 'awscosts', 'ec2prices.json'))
        data = json.load(open(resource_path))
        price = float(data[name]['hourly_price'])
        memory = int(float(data[name]['memory']) * 1024)
        return price, memory

    def get_num_instances(self, reqs):
        return math.ceil(reqs / self.max_reqs_per_second)

    def get_cost_and_num_instances(self, seconds, reqs=None):

        if reqs is not None:
            num_instances = self.get_num_instances(float(reqs)/float(seconds))
        else:
            num_instances = 1

        cost = num_instances * seconds * self._cost_per_second
        return (cost, num_instances)

    def get_cost(self, seconds):
        (cost, _) = self.get_cost_and_num_instances(seconds)
        return cost

    def get_cost_per_second(self, reqs):
        return self.get_num_instances(reqs) * self._cost_per_second

    def get_cost_per_minute(self, reqs):
        # we assume here a uniform distribution of requests
        cost = self.get_cost_per_second(reqs / 60) * 60
        return cost

    def get_cost_per_hour(self, reqs):
        # we assume here a uniform distribution of requests
        cost = self.get_cost_per_second(reqs / 3600) * 3600
        return cost
