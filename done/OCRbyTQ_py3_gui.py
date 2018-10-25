# coding:gbk
import sys
import os
from PIL import Image
import pytesseract
import datetime
import win32api
from PIL import ImageFile
import easygui as g
import tkinter as tk

localPath = g.enterbox(msg="请输入路径",title="OCR图文识别")
yesno = g.buttonbox(msg="请选择识别语言,当前仅支持jpg|jpeg|png|bmp|",title="",choices=("中文","英文","中英文"))
if localPath == '' or localPath == None:
    sys.exit()
root = tk.Tk()
root.title('OCR图片识别')        #窗口标题
root.geometry('400x140')

ImageFile.LOAD_TRUNCATED_IMAGES = True
result = u'图文识别结果.txt'
def insert(s):
    t.insert('end',s)
    t.see('end')
    t.update()
    
t = tk.Text(root,height=10)
t.pack()

def getFileExtension(path):
    return os.path.splitext(path)[1]

def delLineSpace(txt):
    txt = txt.replace(' ','')
    while txt != txt.replace('\n\n','\n'):
        txt = txt.replace('\n\n','\n')
    return txt
      
fp = open(result, 'w')
##localPath=r'C:\Users\admin\Documents\Tencent Files\1327183688\Image\Group\Image3'

sum=0
for dirpath,dirnames,filenames in os.walk(localPath):
    for file in filenames:
            fullpath=os.path.join(dirpath,file)
            fsuffix = getFileExtension(fullpath).lower()            
            if fsuffix == '.jpg' or fsuffix == '.jpeg' or fsuffix == '.png' or fsuffix == '.bmp':
                sum += 1
j=1

for dirpath,dirnames,filenames in os.walk(localPath):
    for file in filenames:
            fullpath=os.path.join(dirpath,file)
            fsuffix = getFileExtension(fullpath).lower()            
            if fsuffix == '.jpg' or fsuffix == '.jpeg' or fsuffix == '.png' or fsuffix == '.bmp':
                #label文本
                txt = '  (%d/%d)%s\n' % (j,sum,file)
                insert(txt)                
##                print('(%d/%d)%s' % (j,sum,file))
                j += 1
                if yesno == '中文':
                    try:
                        text=pytesseract.image_to_string(Image.open(fullpath),lang='chi_sim')##中文chi_sim，英文eng
                    except TypeError:
                        continue
                    if delLineSpace(text) == '':
                        continue
                    text = '【' + fullpath + '】【中文】\n' + delLineSpace(text) + '\n\n'
                    try:
                        fp.write(text)
                    except UnicodeEncodeError:
                        continue
                elif yesno == '英文':
                    text=pytesseract.image_to_string(Image.open(fullpath),lang='eng')
                    if delLineSpace(text) == '':
                        continue
                    text = '【' + fullpath + '】【英文】\n' + delLineSpace(text) + '\n\n'
                    try:
                        fp.write(text)
                    except UnicodeEncodeError:
                        continue
                else:                    
                    textChi = pytesseract.image_to_string(Image.open(fullpath),lang='chi_sim')
                    if delLineSpace(textChi) == '':
                        continue
                    text = '【' + fullpath + '】【中文】\n' + delLineSpace(textChi) + '\n\n'
                    try:
                        fp.write(text)
                    except UnicodeEncodeError:
                        continue
                    textEng = pytesseract.image_to_string(Image.open(fullpath),lang='eng')
                    if delLineSpace(textEng) == '':
                        continue
                    text = '【' + fullpath + '】【英文】\n' + delLineSpace(textEng) + '\n\n'
                    try:
                        fp.write(text)
                    except UnicodeEncodeError:
                        continue
root.destroy()
root.mainloop()
fp.close()
win32api.ShellExecute(0, 'open', 'notepad.exe', u'图文识别结果.txt','',1)


