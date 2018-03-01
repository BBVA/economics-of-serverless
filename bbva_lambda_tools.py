from functools import reduce, partial
import plotly.graph_objs as go
from bbva_colors import BBVAcolors
import awscosts


def devices_func(acc, i):
    if i % 2 == 0:
        acc.append(acc[i - 1] * 2)
    else:
        acc.append(acc[i - 1] * 5)
    return acc


def generate_costs_in_month(
    requests_range,
    flavors, memory,
    time,
    throughput_ratio=1
):
    """Generates EC2 and Lambda costs in a month by a list of requests per
    second.

    Args:
        requests_range (:obj:`list` of :obj:`int`): list of reqs/s.
        flavors (:obj:`list` of :obj:`str`): list of valid EC2 flavors.
        memory
        time (int): duration (in milliseconds) of the Lambda request.
        throughput_ratio (int, optional): 1

    Returns:
        Cost dict:
            - 'lambda':
                - REQS/S_1: COST_IN_DOLLARS
                - REQS/S_2: COST_IN_DOLLARS
                ...
                - REQS/S_n: COST_IN_DOLLARS
            - FLAVOR_1:
                - REQS/S_1: COST_IN_DOLLARS
                ...
            ...

    """
    cost = dict()
    SECONDS_IN_A_MONTH = 3600 * 24 * 30
    # generate costs for EC2 instances:
    for flavor in flavors:
        myec2 = awscosts.EC2(
            flavor,
            MB_per_req=memory,
            ms_per_req=time,
            throughput_ratio=throughput_ratio,
        )
        cost[flavor] = dict()
        for reqs_per_second in requests_range:
            cost[flavor][reqs_per_second] = \
                myec2.get_cost_per_second(reqs_per_second) * SECONDS_IN_A_MONTH

    # generate costs for Lambda:
    mylambda = awscosts.Lambda(
        MB_per_req=memory,
        ms_per_req=time,
    )
    cost['lambda'] = dict()
    for reqs_per_second in requests_range:
        requests_per_month = reqs_per_second * SECONDS_IN_A_MONTH
        cost['lambda'][reqs_per_second] = \
            mylambda.get_cost(requests_per_month, reset_free_tier=True)

    return cost


def draw_costs_by_requests(costs):
    """Generates a Plotly plot object from a cost structure

        Args:
            costs (:obj): Cost data structure with flavors and costs in a month
                per request/s value

        Returns:
            :obj:`plotly.graph_objs.Figure`

    """
    title = 'Monthy cost by number of reqs/s'
    data = []

    color = iter([
        BBVAcolors['light'],
        BBVAcolors['aqua'],
        BBVAcolors['navy'],
        BBVAcolors['coral']
    ])

    for flavor in costs.keys():
        x = list()
        y = list()
        for reqs, price in costs[flavor].items():
            x.append(reqs)
            y.append(price)

        trace = go.Scatter(
            x=x,
            y=y,
            name=flavor,
            marker=next(color)
        )
        data.append(trace)

    layout = go.Layout(
        title=title,
        legend=dict(
            orientation="h",
            y=-.2,
        ),
        width=950,
        height=500,
        xaxis=dict(
            title='<b>reqs/sec</b>',
            type='log'
        ),
        yaxis=dict(
            title='<b>Monthly cost ($)</b>',
            type='log'
        )
    )

    return go.Figure(data=data, layout=layout)


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
    ec2_flavors,
    req_period=None,
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

    title = f'<b>Monthly cost by number of requests per second</b><br>'
    if req_period is not None:
        title +=  f'<i>(request period: {req_period} seconds)</i></b>'

    layout = go.Layout(
        title=title,
        legend=dict(
            orientation="h",
            y=-.2,
        ),
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
