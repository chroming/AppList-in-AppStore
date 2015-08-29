# -*- coding:utf-8 -*-
#使用尝试的方法获取应用信息

import re
import requests
import json


#GetAppURl = requests.get('https://itunes.apple.com/cn/app/id915249333').text
#print GetAppURl
i = 100000000
while i < 999999999:

	print i
	
	try:
		GetAppURL = requests.get('https://itunes.apple.com/cn/lookup?id=%s'%i,timeout=5).text
		print json.loads(GetAppURL)['results'][0]['description']
		i = i + 1
	except:
		i = i + 1
		continue
		