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

from functools import reduce
import awscosts
import bbva_lambda_tools as lambda_tools
from plotly.offline import plot


def main():
    ec2_flavors = ('m3.medium', 'm4.large', 'm4.4xlarge')
    req_period_list = [3600]  # , 8* 3600, 24 * 3600]
    # [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000,
    # 5000000, 10000000]
    num_devices_list = reduce(lambda_tools.devices_func, range(1, 13), [10])
    num_devices_list = list(range(200000, 10000000, 100000))
    resolution = 60 * 5  # in seconds
    interval_duration = 30 * 24 * 3600  # one month in seconds
    lambda_memory = 128
    lambda_request_duration_ms = 200

    ec2_instances = [awscosts.EC2(
        flavor,
        MB_per_req=lambda_memory,
        ms_per_req=lambda_request_duration_ms
    ) for flavor in ec2_flavors]

    for req_period in req_period_list:
        costs = []
        for num_devices in num_devices_list:
            lambda_instance = awscosts.Lambda(
                lambda_memory,
                lambda_request_duration_ms
            )

            # Generate Time Series:
            mean = num_devices // req_period
            devices_time_series = list()
            for i in range(0, (interval_duration // resolution)):
                if i > 0 and i < 1000:
                    devices_time_series.append(mean / 2)
                if i >= 1000 and i < 1500:
                    devices_time_series.append(mean * 2)
                if i >= 1500 and i < 6500:
                    devices_time_series.append(mean / 2)
                if i >= 6500 and i < 8000:
                    devices_time_series.append(mean * 2)
                if i >= 8000:
                    devices_time_series.append(mean / 2)

            cost = lambda_tools.aggregate_costs(
                req_period,
                resolution,
                interval_duration,
                num_devices,
                lambda_instance,
                ec2_instances,
                devices_time_series,
            )

            print(
                cost['hits'],
                cost['reqs_per_second'],
                cost['lambda'],
                cost['ec2_m3.medium_cost'] * cost[f'ec2_m3.medium_instances'],
                cost['ec2_m4.large_cost'] * cost[f'ec2_m4.large_instances'],
                cost['ec2_m4.4xlarge_cost'] * cost[f'ec2_m4.4xlarge_instances']
            )

            costs.append(cost)

        figure = lambda_tools.draw_costs_by_num_devices(
            costs,
            num_devices_list,
            ec2_flavors,
            req_period
        )
        plot(figure)


if __name__ == "__main__":
    main()
