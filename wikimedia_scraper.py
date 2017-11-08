from datetime import datetime, timedelta
from itertools import chain
from functools import reduce
import requests
import re
import os

def time_range(init, end):
    while init<end:
        yield init
        init+=timedelta(hours=1)

def explode_time(date):
    return date, {
        'year': date.year,
        'month': date.month,
        'day': date.day,
        'hour': date.hour,
    }

def gen_dateurl(x):
    ( date, exploded_date ) = x
    ( url_template ) = (
        'https://dumps.wikimedia.org/other/pageviews/'
        '{year}/{year}-{month:02d}/'
        'projectviews-{year}{month:02d}{day:02d}-{hour:02d}0000'
    )
    return date, url_template.format(**exploded_date)

def explode_data_lines(line):
    m = DATALINE_REGEX.match(line)
    return {
        'project': m.group('project'),
        'hits': m.group('hits'),
    }

def explode_data_files(dateurl):
    ( date, url ) = dateurl

    file_name = 'cache/' + url.replace('/','_')

    if not os.path.exists(file_name):
        os.makedirs('cache', exist_ok=True)
        with open(file_name, 'w') as f:
            f.write(requests.get(url).text)
        f.closed

    with open(file_name, 'r') as f:
        file_content = f.read()
    f.closed

    global USE_NOTEBOOK
    if USE_NOTEBOOK:
        global PROGRESS_BAR
        PROGRESS_BAR.value += 1

    match_iter = DATALINE_REGEX.finditer(file_content)

    for match in match_iter:
        yield {
            'project': match.group('project'),
            'hits': match.group('hits'),
            'date': date,
        }

def filter_wikipedia_en(data):
    return data['project'] == 'en'

def output_notebook():
    global USE_NOTEBOOK
    USE_NOTEBOOK = True

def get_traffic_generator(start, end, **kwargs):
    global USE_NOTEBOOK
    global DATALINE_REGEX
    DATALINE_REGEX = re.compile(r'^(?P<project>en|es) - (?P<hits>\d+)', re.MULTILINE)

    try:
        USE_NOTEBOOK
    except NameError:
        USE_NOTEBOOK = False
    else:
        pass

    if USE_NOTEBOOK:
        from ipywidgets import FloatProgress
        from IPython.display import display

        total_files = (end-start).total_seconds()/3600
        global PROGRESS_BAR
        PROGRESS_BAR = FloatProgress(min=0, max=total_files)
        display(PROGRESS_BAR)

    exploded_dates = map(explode_time, time_range(start, end))
    dateurls = map(gen_dateurl, exploded_dates)
    data_generators = map(explode_data_files, dateurls)
    data_generator = reduce(chain, data_generators)
    return data_generator

#for item in data_generator:
#    print(item['date'], item['project'], item['hits'])
