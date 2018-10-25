# coding=gbk

import requests
import re
from xlrd import open_workbook
from xlutils.copy import copy
import xlwt
from bs4 import BeautifulSoup
import json
###--# -*- coding: utf-8 -*-
###--# coding=gbk
###--# coding: utf-8

wb = xlwt.Workbook(encoding='UTF-8', style_compression=0)
sh = wb.add_sheet('data', cell_overwrite_ok=True)
sh.write(0, 0, u'����'.encode('utf-8'))
sh.write(0, 1, u'����'.encode('utf-8'))
sh.write(0, 2, u'ʼ��վ'.encode('utf-8'))
sh.write(0, 3, u'����ʱ��'.encode('utf-8'))
sh.write(0, 4, u'��վʱ��'.encode('utf-8'))
sh.write(0, 5, u'ȫ��ʱ��'.encode('utf-8'))
sh.write(0, 6, u'�յ�վ'.encode('utf-8'))
sh.write(0, 7, u'����ʱ��'.encode('utf-8'))
wb.save(r'myTrain.xls')

def get_html(url):
    heads = {}
    heads['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    requests.adapters.DEFAULT_RETRIES = 5 # ������������
    s = requests.session()
    s.keep_alive = False # �رն�������
    req = s.get(url, headers=heads)
    req.encoding = 'gb2312'
##    req.encoding = 'utf-8'
    html = req.text    
    return html


url='http://www.jt2345.com/huoche/checi/'
html=get_html(url)
soup = BeautifulSoup(html, 'html5lib')
trList = []
n=0
for idx, tr in enumerate(soup.find_all('tr')):
        tds = tr.find_all('td')
        for tdss in tds:
                trList.append(tdss.a.text)
                n+=1
##trList=['1133']

for trs in trList:
    wb = open_workbook("myTrain.xls")
    rows = wb.sheets()[0].nrows
    wbcp = copy(wb)
    sh = wbcp.get_sheet(0)
    
    nurl = u'http://www.jt2345.com/huoche/checi/' + str(trs) + '.htm'
    html=get_html(nurl)
    soup = BeautifulSoup(html, 'html5lib')
    ccList = []
    i = 0
    n = 1
    sh.write(rows,0,str(trs))
    for tr in soup.find_all('tr'):    
        tds = tr.find_all('td')
        if tr.text.find(u'����') == -1:
            for tdss in tds:
                #���˷Ǳ��輰�ظ�����
                if tdss.text !="" and tdss.text.find(u'վվ��ѯ') == -1 and i!=0 and i!=2 and i!=4 and i!=6 and i!=8 and i!=10 and i!=12 and i!=13 and i!=14 and i!=16 and i!=17 and i!=18 and i!=19 and i!=20 and i!=21:
                    sh.write(rows,n,tdss.text)
                    n+=1
                i+=1
    wbcp.save("myTrain.xls")









