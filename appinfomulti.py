# -*- coding:utf-8 -*-
#get the information about all applications in MAC App Store
#multiprocess

import re
import requests
import json

idlist = open('/tmp/applist.txt','r')

def GetValue(ValueName):
    try:
        Value = AppInfo['results'][0][ValueName]
        return Value
    except:
        return None
for id in idlist:
    AppID = id[0:9]
    AppURL = 'https://itunes.apple.com/cn/lookup?id='+AppID
    AppInfoHtml = requests.get(AppURL).text
    AppInfo = json.loads(AppInfoHtml)
    if AppInfo['resultCount'] == 1:

        describe = GetValue('description')
        price = GetValue('price')
        auther = GetValue('artistName')
        version = GetValue('version')
        filesize = GetValue('fileSizeBytes')
        releaseDate = GetValue('releaseDate')[0:10]
        OSrequests = GetValue('minimumOsVersion')
        AppName = GetValue('trackCensoredName')
        print(AppName)
        print(price)

idlist.close()


