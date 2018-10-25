# coding:gb2312
### encoding:cp936
import sys
import os
from PIL import Image
import pytesseract
import datetime
import win32api
from PIL import ImageFile
import tkinter.messagebox

ImageFile.LOAD_TRUNCATED_IMAGES = True
result = u'图文识别结果.txt'

def getFileExtension(path):
    return os.path.splitext(path)[1]

def delLineSpace(txt):
    txt = txt.replace(' ','')
    while txt != txt.replace('\n\n','\n'):
        txt = txt.replace('\n\n','\n')
    return txt
        
fp = open(result, 'w')
localPath=r'C:\Users\admin\Documents\Tencent Files\1327183688\Image\Group'
yesno=tkinter.messagebox.askyesnocancel(u"OCR图文识别by天启",u"请选择识别语言【是】中文【否】英文")
for dirpath,dirnames,filenames in os.walk(localPath):
    for file in filenames:
            fullpath=os.path.join(dirpath,file)
            fsuffix = getFileExtension(fullpath).lower()
            if fsuffix == '.jpg' or fsuffix == '.jpeg' or fsuffix == '.png' or fsuffix == '.bmp':
                print(fullpath)
                if yesno:
                    try:
                        text=pytesseract.image_to_string(Image.open(fullpath),lang='chi_sim')##中文chi_sim，英文eng
                    except TypeError:
                        continue
                    if delLineSpace(text) == '':
##                        text = '【' + fullpath + '】【中文】\n识别为空\n\n'
##                        fp.write(text)
                        continue
                    text = '【' + fullpath + '】【中文】\n' + delLineSpace(text) + '\n\n'
                    try:
                        fp.write(text)
                    except UnicodeEncodeError:
                        continue
##                        text = '【' + fullpath + '】【中文】\n编码错误\n\n'
##                        fp.write(text)
                elif yesno == False:
                    text=pytesseract.image_to_string(Image.open(fullpath),lang='eng')
                    if delLineSpace(text) == '':
##                        text = '【' + fullpath + '】【英文】\n识别为空\n\n'
##                        fp.write(text)
                        continue
                    text = '【' + fullpath + '】【英文】\n' + delLineSpace(text) + '\n\n'
                    try:
                        fp.write(text)
                    except UnicodeEncodeError:
                        continue
##                        text = '【' + fullpath + '】【英文】\n编码错误\n\n'
##                        fp.write(text)
                else:                    
                    textChi = pytesseract.image_to_string(Image.open(fullpath),lang='chi_sim')
                    if delLineSpace(textChi) == '':
##                        text = '【' + fullpath + '】【中文】\n识别为空\n\n'
##                        fp.write(text)
                        continue
                    text = '【' + fullpath + '】【中文】\n' + delLineSpace(textChi) + '\n\n'
                    try:
                        fp.write(text)
                    except UnicodeEncodeError:
                        continue
##                        text = '【' + fullpath + '】【中文】\n编码错误\n\n'
##                        fp.write(text)
                    textEng = pytesseract.image_to_string(Image.open(fullpath),lang='eng')
                    if delLineSpace(textEng) == '':
##                        text = '【' + fullpath + '】【英文】\n识别为空\n\n'
##                        fp.write(text)
                        continue
                    text = '【' + fullpath + '】【英文】\n' + delLineSpace(textEng) + '\n\n'
                    try:
                        fp.write(text)
                    except UnicodeEncodeError:
                        continue
##                        text = '【' + fullpath + '】【英文】\n编码错误\n\n'
##                        fp.write(text)

                    
fp.close()
win32api.ShellExecute(0, 'open', 'notepad.exe', u'图文识别结果.txt','',1)

