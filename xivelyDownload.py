# coding=utf-8
import requests
from config import *
import datetime
import time

out = open('./outPut.csv', 'a')

while (time.mktime(datetime.datetime.strptime(start, "%Y-%m-%dT%H:%M:%SZ").timetuple()) < time.mktime(datetime.datetime.strptime(stop, "%Y-%m-%dT%H:%M:%SZ").timetuple())):
	url = 'https://api.xively.com/v2/feeds/' + feedID + '.csv?start=' + start + '&end=' + str(datetime.datetime.fromtimestamp(time.mktime(datetime.datetime.strptime(start, "%Y-%m-%dT%H:%M:%SZ").timetuple()) + 6*3600).strftime('%Y-%m-%dT%H:%M:%SZ')) + '&limit=1000&interval=0'
	page = requests.get(url, auth=(login, pwd))
	lines = page.content.split('\n')
	for line in lines:
		if(line.split(',')[0] == '2'):
			out.write(line.split(',')[1] + ',' + line.split(',')[2] + '\n')
			cache = line.split(',')[1]
	start = cache.split('.')[0] + 'Z'

out.close()