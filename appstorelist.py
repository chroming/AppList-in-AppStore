# -*- coding:utf-8 -*-
import requests
import re
import time

#get AppStore application name and ID list

Starttime = time.time()

def GetAppList(ListUrl):
    AppListHtml = requests.get(ListUrl).text
    #NextPage = re.findall(r'page\=(\d)\#page',)[-1]
    AppUrlList = re.findall(r'https\:\/\/itunes\.apple\.com\/cn\/app\/[\w\-]*\/id(\d{9})\S{0,9}\>(.*?)\<\/a\>',AppListHtml)
    for AppID in AppUrlList:
        print(AppID[0]+" "+AppID[1])


GetAllList = requests.get('https://itunes.apple.com/cn/genre/mac-you-xi-dong-zuo/id12201?mt=12').text
GetCla = re.findall('genre-nav(.*?)\/div\>',GetAllList,re.S)[0]
GetClass = re.findall('(https\:\/\/itunes\.apple\.com\/cn\/genre\/mac.*?)\"',GetCla,re.S)
for AppClassUrl in GetClass:
    if AppClassUrl != 'https://itunes.apple.com/cn/genre/mac-you-xi/id12006?mt=12':
        for word in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','*']:
            ListUrl = AppClassUrl+"&letter="+word
            GetAppList(ListUrl)

Endtime = time.time()
Usetime = Endtime - Starttime
print Usetime
