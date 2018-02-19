from functools import reduce, partial
import plotly.graph_objs as go
from bbva_colors import BBVAcolors


def devices_func(acc, i):
    if i % 2 == 0:
        acc.append(acc[i - 1] * 2)
    else:
        acc.append(acc[i - 1] * 5)
    return acc


def aggregate_costs(
    req_period,
    resolution,
    interval_duration,
    num_devices,
    lambda_instance,
    ec2_instances_list,
    devices_time_series=None,
    costs_time_series=None,
):

    costs = {}
    costs['resolution_buckets'] = interval_duration // resolution
    costs['hits'] = num_devices * (interval_duration // req_period)
    costs['reqs_per_second'] = costs['hits'] / interval_duration
    costs['lambda'] = lambda_instance.get_cost(
        costs['hits'],
        reset_free_tier=True
    )

    def calc_ec2_instance_use(num_hits, ec2_instance, resolution=0):
        return ec2_instance.get_cost_and_num_instances(
            resolution,
            num_hits * resolution,
        )

    for ec2_instance in ec2_instances_list:

        if devices_time_series is not None:
            calc_by_instance = partial(
                calc_ec2_instance_use,
                ec2_instance=ec2_instance,
                resolution=resolution
            )
            costs_time_series = map(calc_by_instance, devices_time_series)
        else:
            (cost, num_instances) = ec2_instance.get_cost_and_num_instances(
                seconds=resolution,
                reqs=(num_devices // req_period) * resolution
            )
            costs_time_series = \
                [(cost, num_instances)] * (interval_duration // resolution)

        cost, instances = reduce(
            lambda x, y: (
                x[0] + y[0], max(x[1], y[1])
            ),
            costs_time_series,
            (0, 0)
        )

        costs.update({
            f'ec2_{ec2_instance._instance_type}_cost': cost,
            f'ec2_{ec2_instance._instance_type}_instances': instances
        })

    return costs


def draw_costs_by_num_devices(
    costs,
    num_devices_list,
    ec2_flavors,
    req_period,
):
    data = []

    lambda_trace = go.Scatter(
        x=[cost["reqs_per_second"] for cost in costs],
        y=[cost['lambda'] for cost in costs],
        name='Lambda',
        marker=BBVAcolors['coral']
    )
    data.append(lambda_trace)

    for flavor, color in zip(ec2_flavors, ['light', 'aqua', 'navy']):
        trace = go.Scatter(
            x=[cost["reqs_per_second"] for cost in costs],
            y=[cost[f'ec2_{flavor}_cost'] for cost in costs],
            name=f'EC2 {flavor}',
            marker=BBVAcolors[color]
        )
        data.append(trace)

    layout = go.Layout(
        title=f'<b>Monthly cost by number of requests per second</b><br>' +
        f'<i>(request period: {req_period} seconds)</i></b>',
        legend=dict(orientation='h'),
        width=1000,
        height=800,
        xaxis=dict(
            title='<b>Number of reqs/sec</b>',
            type='log'
        ),
        yaxis=dict(
            title='<b>Monthly cost ($)</b>',
            type='log'
        )
    )

    return go.Figure(data=data, layout=layout)
