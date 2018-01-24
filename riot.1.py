from functools import reduce, partial
from random import randint
import math
import plotly
import plotly.graph_objs as go
import awscosts


class Object(object):
    pass


def new_peak(occurrence_periods_range, peak_duration, peak_height):
    peak = Object()
    peak.start = randint(occurrence_periods_range[0], occurrence_periods_range[1])
    peak.end = peak.start + peak_duration
    peak.half = peak.start + peak_duration // 2
    peak.height = peak_height
    return peak

def find_peak(resolution_bucket_index, peaks):
    return next((p for p in peaks if (resolution_bucket_index > p.start and resolution_bucket_index < p.end)), None)
    # for peak in peaks:
    #     if resolution_bucket_index > peak.start and resolution_bucket_index < peak.end:
    #         return peak
    # return None

def num_devices_per_bucket(resolution_bucket_index, total_devices, peak):

    base = total_devices

    if peak is None:
        return base

    if resolution_bucket_index < peak.half:
        return base + math.ceil(total_devices * (peak.height * (resolution_bucket_index / peak.half)))

    return base + math.ceil(total_devices * (peak.height * (peak.half / resolution_bucket_index)))


def generate_requests_time_serie(total_num_devices, request_period, interval_duration, resolution):
    
    #num_periods = interval_duration // request_period
    #peak_duration = interval_duration * 0.15
    peak_duration = interval_duration * 0.15 // resolution # in resolution buckets
    peak_height =  1.6
    hits_distribution = list()
    num_resolution_buckets = interval_duration // resolution
    #infernal_constant = num_periods * (request_period // resolution)
    peaks = list([
        new_peak(range(num_resolution_buckets // 5, num_resolution_buckets // 3), peak_duration, peak_height), 
        new_peak(range(num_resolution_buckets // 2, num_resolution_buckets), peak_duration, peak_height)
        ])


    # Distribute devices in buckets of time deltas from 0 to request_period
    def calculate_buckets(num_devices, request_period):
        device_buckets = [0] * request_period
        for _ in range(0, num_devices):
            pos = randint(0, request_period - 1)
            device_buckets[pos] += 1
        return device_buckets

    resolutions = list()

    for resolution_bucket_index in range(0, num_resolution_buckets):
        peak = find_peak(resolution_bucket_index, peaks)
        num_devices = num_devices_per_bucket(resolution_bucket_index, total_num_devices, peak)
        hits_distribution.append(num_devices)
        devices_buckets = calculate_buckets(num_devices, request_period)
        devices_by_resolution = [max(devices_buckets[p:p+resolution]) for p in range(0, len(devices_buckets), resolution)]

        resolutions = resolutions + devices_by_resolution

    return resolutions, hits_distribution


def aggregate_costs(req_period, resolution, interval_duration, hits, lambda_instance, ec2_instances_list, devices_time_serie):
    costs = {'num_resolution_buckets':0, 'hits':0, 'lambda':0}
    costs['num_resolution_buckets'] = interval_duration // resolution
    costs['hits'] = hits
    costs['reqs_per_second'] = costs['hits'] / interval_duration
    costs['lambda'] = lambda_instance.get_cost(costs['hits'], reset_free_tier=True)

    def calc_ec2_instance_use(num_hits, ec2_instance = None, resolution = 0):
        num_instances = max(1, ec2_instance.get_num_instances(num_hits/resolution))
        cost = ec2_instance._cost_per_hour/resolution *  (num_instances - 1) # we accumulate only auto-scaled instances (>1)
        return (num_instances, cost)

    for ec2_instance in ec2_instances_list:
        calc_by_instance = partial(calc_ec2_instance_use, ec2_instance = ec2_instance, resolution = resolution)
        instances_and_cost = reduce(lambda x, y:  (max(x[0],y[0]), x[1] + y[1]), map(calc_by_instance, devices_time_serie), (0, 0))
        cost = (ec2_instance._cost_per_hour * (interval_duration / 3600)) + instances_and_cost[1] # the cost of one fixed instance plus the cost of the auto-scaled ones
        costs.update({
            f'ec2_{ec2_instance._instance_type}_cost':cost,
            f'ec2_{ec2_instance._instance_type}_instances':instances_and_cost[0]
            })
    
    return costs

def draw_costs_by_num_devices(costs, num_devices_list, ec2_flavors, req_period):

    data = []

    lambda_trace = go.Scatter(
        x=[cost["reqs_per_second"] for cost in costs],
        y=[cost['lambda'] for cost in costs],
        name='Lambda'
    )
    data.append(lambda_trace)

    for flavor in ec2_flavors:
        trace1 = go.Scatter(
            x=[cost["reqs_per_second"] for cost in costs],
            y=[cost[f'ec2_{flavor}_cost'] * cost[f'ec2_{flavor}_instances'] for cost in costs],
            name=f'EC2 {flavor}',
            showlegend=False
        )
        trace2 = go.Scatter(
            x=num_devices_list,
            y=[cost[f'ec2_{flavor}_cost'] * cost[f'ec2_{flavor}_instances'] for cost in costs],
            name=f'EC2 {flavor}',
            xaxis='x2'
        )
        data.append(trace1)
        data.append(trace2)

    layout = go.Layout(
        title=f'Cost by number of devices (request period: {req_period} seconds)',
        legend=dict(orientation='h'),
        width=1000,
        height=800,
        margin=go.Margin(
            t=200,
            b=200,
            r=100,
            l=100,
            autoexpand=False
        ),
        xaxis=dict(
            title='Number of reqs/sec',
            type='log',
            anchor='free',
            position=0.02
        ),
        xaxis2=dict(
            title="Number of devices",
            type='log',
            side='top',
            overlaying='x'
        ),
        yaxis=dict(
            title='Cost ($)'
        )
    )

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig)

def draw_num_devices(mydata):
    data = []

    devices_trace = go.Scatter(
        y=mydata,
        x=[i for i in range(0, len(mydata))],
        name='Data',
        fill="tozeroy"
    )
    data.append(devices_trace)


    layout = go.Layout(
        title=f'Number of devices over periods',
        legend=dict(orientation="h"),
        width=1000,
        height=800,
        xaxis=dict(
            title='Periods',
            autorange=True
        ),
        yaxis=dict(
            title='Devices (#)'
        )
    )

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig)

def main():

    def devices_func(acc, i):
        if i % 2 == 0:
            acc.append(acc[i-1] * 2)
        else:
            acc.append(acc[i-1] * 5)
        return acc

    ec2_flavors = ('m3.medium', 'm4.large', 'm4.4xlarge')
    req_period_list = [24 * 3600, 7*24*3600]
    #[10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]
    num_devices_list = reduce(devices_func, range(1,5), [1000000]) # [1000000, 10000000, 100000000 ] 
    print(num_devices_list)

    resolution = 60 * 60 * 24 # in seconds
    interval_duration = 30 * 24 * 3600 # one month in seconds
    lambda_memory = 128
    lambda_request_duration_ms = 200
    ec2_instances = [awscosts.EC2(flavor, MB_per_req=lambda_memory, ms_per_req=lambda_request_duration_ms) for flavor in ec2_flavors]

    for req_period in req_period_list:
        costs = []
        for num_devices in num_devices_list:
            lambda_instance = awscosts.Lambda(lambda_memory, lambda_request_duration_ms)
            time_serie, hits_distribution = generate_requests_time_serie(num_devices, req_period, interval_duration, resolution)
            draw_num_devices(time_serie)
            cost = aggregate_costs(req_period, resolution, interval_duration, sum(hits_distribution), lambda_instance, ec2_instances, time_serie)

            print(cost)
            costs.append(cost)

        draw_costs_by_num_devices(costs, num_devices_list, ec2_flavors, req_period)

if __name__ == "__main__":
    main()
