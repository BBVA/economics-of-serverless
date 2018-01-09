import pandas as pd
from datetime import datetime
from functools import reduce
from itertools import groupby, chain
from random import randint
from datetime import timedelta
import math
import numpy as np

from iot.simulator import *

import awscosts

class Model:
	device_number = 0
	request_period_in_seconds = 0
	period_start = 0
	period_end = 0
	resolution_in_seconds = 0
	MB_per_req= 0
	ms_per_req = 0
	
	def __init__(self, n, p, s, e, r, mb, ms):
		self.device_number = n
		self.request_period_in_seconds = p
		self.period_start = s
		self.period_end = e
		self.resolution_in_seconds = r
		self.MB_per_req= mb
		self.ms_per_req = ms
		
def new_model(n, p, d, r, mb, ms):
	today = datetime.today()
	start = datetime(today.year,1, 1)
	end = start + timedelta(days=d)
	return Model(n, p, start, end, r, mb, ms)
		
def generate(model):
	mylambda = awscosts.Lambda(MB_per_req=model.MB_per_req, ms_per_req=model.ms_per_req)
	# Create device fleet generator (lazy generates a collection of time deltas)
	devices = devices_generator(model.device_number, model.request_period_in_seconds)
	
	# Create a generator for device periodic requests
	request_period_generator = time_walker(model.period_start, model.request_period_in_seconds, model.period_end)

	# Create a "stamper" that fixes deltas into actual datetime stamps for a specific period
	stamper = devices_date_stamper(devices)

	
	# Create a function that returns the t0 of a period for a given time
	resolution_finder = resolution_period_finder(model.period_start, model.resolution_in_seconds)

	# flatMap = map + reduce
	all_requests = reduce(chain, map(stamper, request_period_generator), iter([]))
	
	requests_by_resolution = map(lambda x: (x[0],len(list(x[1]))), groupby(all_requests, resolution_finder))


	return pd.DataFrame.from_records(list(requests_by_resolution), index='date', columns=['date', 'hits'])

def costs(model, df):
	
	mylambda = awscosts.Lambda(MB_per_req=model.MB_per_req, ms_per_req=model.ms_per_req)
	myec2 = awscosts.EC2(instance_type='m4.4xlarge', MB_per_req=model.MB_per_req/10)

	df['date'] = df.index

	
	def myl(x):
		return x['date'], x['hits'], mylambda.get_hourly_cost(date = x['date'], reqs = x['hits']), myec2.get_cost_per_second(reqs = x['hits'])*model.resolution_in_seconds, myec2.get_instances(reqs = x['hits'])
		
	df['lambda_cost'] = 0
	df['ec2_cost'] = 0
	df['instances'] = 0


	
	df[['date','hits','lambda_cost','ec2_cost','instances']] = df.apply(myl, axis=1)
	
	return df


	
	
def main():
	freq_list=[60,3600, 8*3600, 24*3600]
	devices_list=[10,100,1000,10000,100000,1000000]
	for p in freq_list:
		for n in devices_list:
			model = new_model(n,p,30,60,128,200)
			df = costs(model,generate(model))
			print(df["hits"].sum(),df["lambda_cost"].sum(),df["ec2_cost"].sum(), p)
			
	
if __name__ == "__main__":
	main()
    
