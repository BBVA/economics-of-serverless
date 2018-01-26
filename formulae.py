import math
import time
from functools import partial
import plotly
from plotly import tools
import plotly.graph_objs as go

def lambda_f(num_requests, memory_size):
    return max(0, (((num_requests * 0.2) * (memory_size / 1024)) - 400000) * 0.0000167 + ((num_requests - 1000000) * (0.2 / 1000000)))

def ec2_f(reqs_per_second, max_reqs_per_second = 0, price_per_hour = 0):
    price_per_month = price_per_hour * 24 * 30
    num_instances = max(1, reqs_per_second // max_reqs_per_second)
    return num_instances * price_per_month

def calc_max_reqs_per_second(throughput_ratio, ec2_memory_size, lambda_size):
    return (ec2_memory_size / lambda_size) * throughput_ratio # throughput ratio between ec2 and lambda

def draw_costs_by_reqs_per_second(costs):

    titles = []
    for cost in costs:
        titles.append(f'<i>memory: {cost.lambda_size}MB</i><br><i>throughput ratio: {cost.throughput_ratio}</i>')

    fig = tools.make_subplots(rows = 3, cols = 1, subplot_titles = titles, shared_xaxes=False)

    for row, cost in enumerate(costs):
        titles = []
        showlegend = True if row == 2 else False
        lambda_trace = go.Scatter(
            x=[c["reqs_per_second"] for c in cost.data],
            y=[c['lambda_cost'] for c in cost.data],
            name='<b>Lambda</b>',
            showlegend=showlegend,
            marker=dict(color='blue')
        )
        
        fig.append_trace(lambda_trace, row + 1, 1)

        for flavor, color in [('m3_medium', 'green'), ('m4_large', 'orange'), ('m4_4xlarge', 'red')]:
            trace = go.Scatter(
                x=[c["reqs_per_second"] for c in cost.data],
                y=[c[f'ec2_{flavor}_cost'] for c in cost.data],
                name=f'<b>EC2 {flavor}</b>',
                showlegend=showlegend,
                marker=dict(color=color)
            )
            fig.append_trace(trace, row + 1, 1)
            

    fig['layout'].update(
        title='<b>Monthly cost by number of requests per second</b>',
        legend=dict(
            orientation='v'
        ),
        width=800,
        height=1000,
        # margin=go.Margin(
        #     t=200,
        #     b=200,
        #     r=100,
        #     l=100,
        #     autoexpand=False
        # ),
        xaxis1=dict(
            title='<b>Number of reqs/sec</b>',
            type='log'
        ),
        xaxis2=dict(
            title='<b>Number of reqs/sec</b>',
            type='log'
        ),
        xaxis3=dict(
            title='<b>Number of reqs/sec</b>',
            type='log'
        ),
        yaxis1=dict(
            title='<b>Monthly cost ($)</b>',
            type='log'
        ),
        yaxis2=dict(
            title='<b>Monthly cost ($)</b>',
            type='log'
        ),
        yaxis3=dict(
            title='<b>Monthly cost ($)</b>',
            type='log'
        )
    )
    plotly.offline.plot(fig)

class Cost:

    def __init__(self, lambda_size = 0, throughput_ratio = 0):
        self.data = []
        self.lambda_size = lambda_size
        self.throughput_ratio = throughput_ratio
        
    def append_data(self, data):
        self.data.append(data)    

    

def main():

    interval = 30 * 24 * 3600
    memory_sizes = [128, 256, 512]

    for memory_size in memory_sizes:

        ec2_m3_medium_max_reqs = partial(calc_max_reqs_per_second, ec2_memory_size = 3500, lambda_size = memory_size)
        ec2_m4_large_max_reqs = partial(calc_max_reqs_per_second, ec2_memory_size = 8000, lambda_size = memory_size)
        ec3_m4_4xlarge_max_reqs = partial(calc_max_reqs_per_second, ec2_memory_size = 64000, lambda_size = memory_size)

        costs = []

        for throughput_ratio in [1, 5, 10]:

            ec2_m3_medium_f = partial(ec2_f, max_reqs_per_second = ec2_m3_medium_max_reqs(throughput_ratio), price_per_hour = 0.067)
            ec2_m4_large_f = partial(ec2_f, max_reqs_per_second =  ec2_m4_large_max_reqs(throughput_ratio), price_per_hour = 0.1)
            ec2_m4_4xlarge_f = partial(ec2_f, max_reqs_per_second =  ec3_m4_4xlarge_max_reqs(throughput_ratio), price_per_hour = 0.8)

            cost = Cost(lambda_size = memory_size, throughput_ratio = throughput_ratio)

            for reqs_per_second in range(5, 3000):
                cost_data = {'reqs_per_second':0, 'lambda_cost':0, 'ec2_m3_medium_cost':0, 'ec2_m4_large_cost':0, 'ec2_m4_4xlarge_cost':0}
                num_requests = reqs_per_second * interval
                cost_data['reqs_per_second'] = reqs_per_second
                cost_data['lambda_cost'] = lambda_f(num_requests, memory_size)
                cost_data['ec2_m3_medium_cost'] = ec2_m3_medium_f(reqs_per_second)
                cost_data['ec2_m4_large_cost'] = ec2_m4_large_f(reqs_per_second)
                cost_data['ec2_m4_4xlarge_cost'] = ec2_m4_4xlarge_f(reqs_per_second)
                cost.append_data(cost_data)
                print(cost_data)

            costs.append(cost)

        time.sleep(1)
        draw_costs_by_reqs_per_second(costs)

if __name__ == "__main__":
    main()