import math
from functools import partial
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

def lambda_f(num_requests, memory_size):
    return max(0, (((num_requests * 0.2) * (memory_size / 1024)) - 400000) * 0.0000167 + ((num_requests - 1000000) * (0.2 / 1000000)))

def ec2_f(reqs_per_second, max_reqs_per_second = 0, price_per_hour = 0):
    price_per_month = price_per_hour * 24 * 30
    num_instances = max(1, reqs_per_second // max_reqs_per_second)
    return num_instances * price_per_month

def calc_max_reqs_per_second(throughput_ratio, ec2_memory_size, lambda_size):
    return (ec2_memory_size / lambda_size) * throughput_ratio # throughput ratio between ec2 and lambda

def draw_costs_by_reqs_per_second(costs, throughput_ratio):

    data = []

    lambda_trace = go.Scatter(
        x=[cost["reqs_per_second"] for cost in costs],
        y=[cost['lambda_cost'] for cost in costs],
        name='<b>Lambda</b>'
    )
    data.append(lambda_trace)

    for flavor in ['m3_medium', 'm4_large', 'm4_4xlarge']:
        trace1 = go.Scatter(
            x=[cost["reqs_per_second"] for cost in costs],
            y=[cost[f'ec2_{flavor}_cost'] for cost in costs],
            name=f'<b>EC2 {flavor}</b>',
            showlegend=True
        )
        data.append(trace1)

    layout = go.Layout(
        title=f'<b>Monthly cost by number of requests per second</b> <br><i>(throughput ratio of ec2 instances to lambda: {throughput_ratio}</i>)',
        legend=dict(
            orientation='h',
            y=-0.2
        ),
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
            title='<b>Number of reqs/sec</b>',
            type='log'
        ),
        yaxis=dict(
            title='<b>Monthly cost ($)</b>'
        )
    )

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig)

def main():

    interval = 30 * 24 * 3600
    memory_sizes = [128, 256, 512]

    for memory_size in memory_sizes:

        ec2_m3_medium_max_reqs = partial(calc_max_reqs_per_second, ec2_memory_size = 3500, lambda_size = memory_size)
        ec2_m4_large_max_reqs = partial(calc_max_reqs_per_second, ec2_memory_size = 8000, lambda_size = memory_size)
        ec3_m4_4xlarge_max_reqs = partial(calc_max_reqs_per_second, ec2_memory_size = 64000, lambda_size = memory_size)

        for throughput_ratio in [1, 5, 10]:

            ec2_m3_medium_f = partial(ec2_f, max_reqs_per_second = ec2_m3_medium_max_reqs(throughput_ratio), price_per_hour = 0.067)
            ec2_m4_large_f = partial(ec2_f, max_reqs_per_second =  ec2_m4_large_max_reqs(throughput_ratio), price_per_hour = 0.1)
            ec2_m4_4xlarge_f = partial(ec2_f, max_reqs_per_second =  ec3_m4_4xlarge_max_reqs(throughput_ratio), price_per_hour = 0.8)

            costs = []
            for reqs_per_second in range(0, 3000):
                cost = {'reqs_per_second':0, 'lambda_cost':0, 'ec2_m3_medium_cost':0, 'ec2_m4_large_cost':0, 'ec2_m4_4xlarge_cost':0}
                num_requests = reqs_per_second * interval
                cost['reqs_per_second'] = reqs_per_second
                cost['lambda_cost'] = lambda_f(num_requests, memory_size)
                cost['ec2_m3_medium_cost'] = ec2_m3_medium_f(reqs_per_second)
                cost['ec2_m4_large_cost'] = ec2_m4_large_f(reqs_per_second)
                cost['ec2_m4_4xlarge_cost'] = ec2_m4_4xlarge_f(reqs_per_second)
                costs.append(cost)
                print(cost)

            draw_costs_by_reqs_per_second(costs, throughput_ratio)

if __name__ == "__main__":
    main()