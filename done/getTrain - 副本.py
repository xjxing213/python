# -*- coding: utf-8 -*-
import requests
import re
from xlrd import open_workbook
from xlutils.copy import copy
import xlwt
from bs4 import BeautifulSoup
import json
import chardet

def get_html(url):
    heads = {}
    heads['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    req = requests.get(url, headers=heads)
    req.encoding = 'gb2312'
##    req.encoding = 'gb2312'
##    req.encoding = 'utf-8'
    html = req.text    
    return html


##url='http://www.jt2345.com/huoche/checi/'
##html=get_html(url)
####soup = BeautifulSoup(html,'lxml')
##soup = BeautifulSoup(html, 'html5lib')
##data_list = []
##n=0
##for idx, tr in enumerate(soup.find_all('tr')):
##        tds = tr.find_all('td')
##        for tdss in tds:
##                data_list.append(tdss.a.text)
##                n+=1
data_list=['1133']

for cc in data_list:        
        nurl = u'http://www.jt2345.com/huoche/checi/' + str(data_list[0]) + '.htm'
        html=get_html(nurl)
        soup = BeautifulSoup(html, 'html5lib')
        ccList = []
        i=0
        for tr in soup.find_all('tr'):
                tds = tr.find_all('td')
                if tr.text.find(u'车次') == -1:
                        for tdss in tds:
                                if i == 1:
                                        print tdss.text.encode('gb2312')
                                        ccList.append({'车型':tdss.text.encode('gb2312')})
                                if i == 3:
                                        ccList.append({'始发站':tdss.text.encode('gb2312')})
                                if i == 5:
                                        ccList.append({'发车时间':tdss.text.encode('gb2312')})
                                if i == 7:
                                        ccList.append({'到站时间':tdss.text.encode('gb2312')})
                                if i == 9:
                                        ccList.append({'全程时间':tdss.text.encode('gb2312')})
                                if i == 11:
                                        ccList.append({'终点站':tdss.text.encode('gb2312')})                                        
                                i+=1
print unicode(ccList[0]).encode("UTF-8")








