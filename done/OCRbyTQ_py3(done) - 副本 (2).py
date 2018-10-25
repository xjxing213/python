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
result = u'ͼ��ʶ����.txt'

def getFileExtension(path):
    return os.path.splitext(path)[1]

def delLineSpace(txt):
    txt = txt.replace(' ','')
    while txt != txt.replace('\n\n','\n'):
        txt = txt.replace('\n\n','\n')
    return txt
        
fp = open(result, 'w')
localPath=r'C:\Users\admin\Documents\Tencent Files\1327183688\Image\Group'
yesno=tkinter.messagebox.askyesnocancel(u"OCRͼ��ʶ��by����",u"��ѡ��ʶ�����ԡ��ǡ����ġ���Ӣ��")
for dirpath,dirnames,filenames in os.walk(localPath):
    for file in filenames:
            fullpath=os.path.join(dirpath,file)
            fsuffix = getFileExtension(fullpath).lower()
            if fsuffix == '.jpg' or fsuffix == '.jpeg' or fsuffix == '.png' or fsuffix == '.bmp':
                print(fullpath)
                if yesno:
                    try:
                        text=pytesseract.image_to_string(Image.open(fullpath),lang='chi_sim')##����chi_sim��Ӣ��eng
                    except TypeError:
                        continue
                    if delLineSpace(text) == '':
##                        text = '��' + fullpath + '�������ġ�\nʶ��Ϊ��\n\n'
##                        fp.write(text)
                        continue
                    text = '��' + fullpath + '�������ġ�\n' + delLineSpace(text) + '\n\n'
                    try:
                        fp.write(text)
                    except UnicodeEncodeError:
                        continue
##                        text = '��' + fullpath + '�������ġ�\n�������\n\n'
##                        fp.write(text)
                elif yesno == False:
                    text=pytesseract.image_to_string(Image.open(fullpath),lang='eng')
                    if delLineSpace(text) == '':
##                        text = '��' + fullpath + '����Ӣ�ġ�\nʶ��Ϊ��\n\n'
##                        fp.write(text)
                        continue
                    text = '��' + fullpath + '����Ӣ�ġ�\n' + delLineSpace(text) + '\n\n'
                    try:
                        fp.write(text)
                    except UnicodeEncodeError:
                        continue
##                        text = '��' + fullpath + '����Ӣ�ġ�\n�������\n\n'
##                        fp.write(text)
                else:                    
                    textChi = pytesseract.image_to_string(Image.open(fullpath),lang='chi_sim')
                    if delLineSpace(textChi) == '':
##                        text = '��' + fullpath + '�������ġ�\nʶ��Ϊ��\n\n'
##                        fp.write(text)
                        continue
                    text = '��' + fullpath + '�������ġ�\n' + delLineSpace(textChi) + '\n\n'
                    try:
                        fp.write(text)
                    except UnicodeEncodeError:
                        continue
##                        text = '��' + fullpath + '�������ġ�\n�������\n\n'
##                        fp.write(text)
                    textEng = pytesseract.image_to_string(Image.open(fullpath),lang='eng')
                    if delLineSpace(textEng) == '':
##                        text = '��' + fullpath + '����Ӣ�ġ�\nʶ��Ϊ��\n\n'
##                        fp.write(text)
                        continue
                    text = '��' + fullpath + '����Ӣ�ġ�\n' + delLineSpace(textEng) + '\n\n'
                    try:
                        fp.write(text)
                    except UnicodeEncodeError:
                        continue
##                        text = '��' + fullpath + '����Ӣ�ġ�\n�������\n\n'
##                        fp.write(text)

                    
fp.close()
win32api.ShellExecute(0, 'open', 'notepad.exe', u'ͼ��ʶ����.txt','',1)

