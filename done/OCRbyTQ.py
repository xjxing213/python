# encoding:cp936
### coding: utf8
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

def getCoding(strInput):
    if isinstance(strInput, unicode):
        return "unicode"
    try:
        strInput.decode("utf8")
        return 'utf8'
    except:
        pass
    try:
        strInput.decode("gbk")
        return 'gbk'
    except:
        pass
        
def tran2UTF8(strInput):
    strCodingFmt = getCoding(strInput)
    if strCodingFmt == "utf8":
        return strInput
    elif strCodingFmt == "unicode":
        return strInput.encode("utf8")
    elif strCodingFmt == "gbk":
        return strInput.decode("gbk").encode("utf8")

def tran2GBK(strInput):
    strCodingFmt = getCoding(strInput)
    if strCodingFmt == "gbk":
        return strInput
    elif strCodingFmt == "unicode":
        return strInput.encode("gbk")
    elif strCodingFmt == "utf8":
        return strInput.decode("utf8").encode("gbk")

fp = open(result, 'w')
localPath=os.getcwd()
yesno=tkinter.messagebox.askyesnocancel(u"OCRͼ��ʶ��by����",u"��ѡ��ʶ�����ԡ��ǡ����ġ���Ӣ��")
for dirpath,dirnames,filenames in os.walk(localPath):
    for file in filenames:
            fullpath=os.path.join(dirpath,file)
            fsuffix = getFileExtension(fullpath).lower()
            if fsuffix == '.jpg' or fsuffix == '.jpeg' or fsuffix == '.png' or fsuffix == '.bmp':
                print fullpath
                if yesno:
                    text=pytesseract.image_to_string(Image.open(fullpath),lang='chi_sim')##����chi_sim��Ӣ��eng
                    text = '��' + fullpath + '��\n' + text.encode('gb2312') + '\n\n'
                elif yesno == False:
                    text=pytesseract.image_to_string(Image.open(fullpath),lang='eng')
                    text = '��' + fullpath + '��\n' + tran2UTF8(text) + '\n\n'
                else:
                    textChi = pytesseract.image_to_string(Image.open(fullpath),lang='chi_sim')
                    textEng = pytesseract.image_to_string(Image.open(fullpath),lang='eng')
                    text = u'�����ġ�\n' + tran2UTF8(textChi) + u'\n��Ӣ�ġ�\n' + tran2UTF8(textEng)
                    text = '��' + fullpath + '��\n' + text + '\n\n'
                fp.write(text)
fp.close()
win32api.ShellExecute(0, 'open', 'notepad.exe', u'ͼ��ʶ����.txt','',1)

