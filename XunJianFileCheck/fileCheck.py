# coding=utf-8
import sys
import os
import easygui as g


def checkDel(lst,l):
    if l in lst:
        lst.remove(l)

def getTxtFileList(fdir):
    flist = []
    fp = open(fdir, 'r')
    ft = fp.read()
    arr = ft.split('\n')
    for line in arr:
        line = line.replace(' ','').replace('|','').replace('-','').replace('└','').replace('│','').replace('├','').replace('─','')
        if line != '':            
            flist.append(line)
    fp.close()
    #剔除目录
    for l in flist:
        if l.find('.') == -1:
            flist.remove(l)            
    return flist

def getDirFileList(tdir):    
    flist = []
    for dirpath,dirnames,filenames in os.walk(tdir):
        for file in filenames:
            fullpath=os.path.join(dirpath,file)
            file=file.replace('-','').replace(' ','')
            if file[-3:] != 'zip' and file[-3:] != 'exe' and file[-3:] != '.py':
                if file[:17] == '【L网周检】L网中兴license':
                    flist.append('【L网周检】L网中兴license')
                elif file[:17] == '【L网周检】L网华为license':
                    flist.append('【L网周检】L网华为license')
                else:
                    flist.append(file)

    checkDel(flist,'fileCheck.py')
    return flist


thedir=os.getcwd()
errorlist = []
dirfilelist = getDirFileList(thedir)
for l in dirfilelist:
    hz = l[-3:].lower()
    if hz != 'exe' and hz != 'png' and hz != 'bmp' and hz != 'lsx' and hz != 'xls'and hz != 'txt' and hz != 'nse':
        errorlist.append('存在非法文件：' + str(l))
        dirfilelist.remove(l)

txtdir = os.path.join(thedir,'周检目录.txt')
txtfilelist = getTxtFileList(txtdir)
dirfilelist = getDirFileList(thedir)
for tl in txtfilelist:
    if tl not in dirfilelist and tl[:17] not in dirfilelist:
        errorlist.append(str(tl) + '：文件不存在，请补充')

mymsg = ''
if errorlist == []:
    mymsg = '恭喜，检测无异常！'
else:
    for e in errorlist:
        mymsg = mymsg + e + '\n'
g.msgbox(msg=mymsg,title="检测结果！",ok_button="确定")


























