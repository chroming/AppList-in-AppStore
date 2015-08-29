# -*- coding:utf-8 -*-
import requests
import re
#用于抓取AppStore应用列表和ID


def GetAppList(ListUrl):
	AppListHtml = requests.get(ListUrl).text
	#NextPage = re.findall(r'page\=(\d)\#page',)[-1]	
	AppUrlList = re.findall(r'https\:\/\/itunes\.apple\.com\/cn\/app\/[\w\-]*\/id(\d{9})\S{0,9}\>(.*?)\<\/a\>',AppListHtml)
	for AppID in AppUrlList:
		print(AppID[0]+" "+AppID[1])
		

GetAllList = requests.get('https://itunes.apple.com/cn/genre/mac-shang-wu/id12001').text
#print GetAllList
GetCla = re.findall('genre-nav(.*?)\/div\>',GetAllList,re.S)[0]
GetClass = re.findall('(https\:\/\/itunes\.apple\.com\/cn\/genre\/mac.*?)\"',GetCla,re.S)
for AppClassUrl in GetClass:
	#print AppClassUrl
	for word in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','*']:
		ListUrl = AppClassUrl+"&letter="+word
		GetAppList(ListUrl)
