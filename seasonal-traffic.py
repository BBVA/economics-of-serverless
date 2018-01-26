import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np



def get_traffic(num_devices, request_period, interval_duration, resolution):
    mean = num_devices // request_period
    traffic = list()
    for i in range(0,(interval_duration//resolution)):
        if i > 0 and i < 1000:
            traffic.append(mean/2)
        if i >= 1000 and i < 1500:
            traffic.append(mean*2)
        if i >=1500 and i < 6500:
            traffic.append(mean/2)
        if i >= 6500 and i <8000:
            traffic.append(mean*2)
        if i >=8000:
            traffic.append(mean/2)
    return traffic

def draw(traffic):

    data = []

    trace = go.Scatter(
        x=list(range(len(traffic))),
        y=traffic,
        name='Lambda'
    )
    data.append(trace)

    layout = go.Layout(
        title=f'<b>Traffic distribution</b><br> <i>Devices: 1M ,Request period: 1h, Interval: 30 days, Resolution: 5min</i>',
        legend=dict(orientation='v'),
        width=800,
        height=800,
        yaxis=dict(
            title='<b>Requests (#)</b>',
        ),
        xaxis=dict(
            title="<b>Time (s)</b>",
        )
    )

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig)


def main():
    draw(get_traffic(1000000, 3600, 30*24*3600, 300))

if __name__ == "__main__":
    main()

