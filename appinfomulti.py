# -*- coding:utf-8 -*-
#get the information about all applications in MAC App Store
#multiprocess
#多进程版，仅限OSX或Linux使用。

import re
import requests
import json
import os

#输入进程数及读入列表文本
c = int(raw_input("please input process number"))
idlist = open('/tmp/applist.txt','r')
idline = idlist.readlines()
linelen = len(idline)

#初始化切片间隔
k = c

#从json返回值函数
def GetValue(AppInfo,ValueName):
    try:
        Value = AppInfo['results'][0][ValueName]
        return Value
    except:
        return None

#依次获取页面函数
def info(c):
    for id in idline[c-1:linelen:k]:
        #获取页面并转换

        AppID = id[0:9]
        AppURL = 'https://itunes.apple.com/cn/lookup?id='+AppID
        try:
            AppInfoHtml = requests.get(AppURL,timeout=10).text
            AppInfo = json.loads(AppInfoHtml)
        except:
            AppInfo = {'resultCount':'0'}
        #根据页面内容获取各项
        if AppInfo['resultCount'] == 1:

            #describe = GetValue(AppInfo,'description')
            price = GetValue(AppInfo,'price')
            auther = GetValue(AppInfo,'artistName')
            version = GetValue(AppInfo,'version')
            filesize = GetValue(AppInfo,'fileSizeBytes')
            releaseDate = GetValue(AppInfo,'releaseDate')[0:10]
            OSrequests = GetValue(AppInfo,'minimumOsVersion')
            AppName = GetValue(AppInfo,'trackCensoredName')
            rate = GetValue(AppInfo,'averageUserRating')
            ratenumber = GetValue(AppInfo,'userRatingCount')
            print(AppName+"#"+version+"#"+releaseDate+"#"+OSrequests+"#"+filesize+"#"+auther+"#"+str(price)+"#"+rate+"#"+ratenumber)

                    
#多进程函数
def osfork(c):
    if c == 0:
        raw_input("wait……")
    else:
        pid = os.fork()
        if pid == 0:
            info(c)
        else:
            c = c - 1
            osfork(c)

osfork(c)
idlist.close()


