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

import plotly
import plotly.graph_objs as go


def get_traffic(num_devices, request_period, interval_duration, resolution):
    mean = num_devices // request_period
    traffic = list()
    for i in range(0, (interval_duration // resolution)):
        if i > 0 and i < 1000:
            traffic.append(mean / 2)
        if i >= 1000 and i < 1500:
            traffic.append(mean * 2)
        if i >= 1500 and i < 6500:
            traffic.append(mean/2)
        if i >= 6500 and i < 8000:
            traffic.append(mean * 2)
        if i >= 8000:
            traffic.append(mean / 2)
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
        title=f'<b>Traffic distribution</b><br>'
        '<i>Devices: 1m, '
        'Request period: 1h, '
        'Interval: 30 days, '
        'Resolution: 5 min</i>',
        legend=dict(orientation='v'),
        width=800,
        height=800,
        yaxis=dict(
            title='<b># Requests</b>',
        ),
        xaxis=dict(
            title="<b>Time (s)</b>",
        ),
    )

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig)


def main():
    draw(get_traffic(1E6, 3600, 30*24*3600, 300))


if __name__ == "__main__":
    main()
