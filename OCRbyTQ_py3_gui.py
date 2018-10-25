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

localPath = g.enterbox(msg="������·��",title="OCRͼ��ʶ��")
yesno = g.buttonbox(msg="��ѡ��ʶ������,��ǰ��֧��jpg|jpeg|png|bmp|",title="",choices=("����","Ӣ��","��Ӣ��"))
if localPath == '' or localPath == None:
    sys.exit()
root = tk.Tk()
root.title('OCRͼƬʶ��')        #���ڱ���
root.geometry('400x140')

ImageFile.LOAD_TRUNCATED_IMAGES = True
result = u'ͼ��ʶ����.txt'
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
                #label�ı�
                txt = '  (%d/%d)%s\n' % (j,sum,file)
                insert(txt)                
##                print('(%d/%d)%s' % (j,sum,file))
                j += 1
                if yesno == '����':
                    try:
                        text=pytesseract.image_to_string(Image.open(fullpath),lang='chi_sim')##����chi_sim��Ӣ��eng
                    except TypeError:
                        continue
                    if delLineSpace(text) == '':
                        continue
                    text = '��' + fullpath + '�������ġ�\n' + delLineSpace(text) + '\n\n'
                    try:
                        fp.write(text)
                    except UnicodeEncodeError:
                        continue
                elif yesno == 'Ӣ��':
                    text=pytesseract.image_to_string(Image.open(fullpath),lang='eng')
                    if delLineSpace(text) == '':
                        continue
                    text = '��' + fullpath + '����Ӣ�ġ�\n' + delLineSpace(text) + '\n\n'
                    try:
                        fp.write(text)
                    except UnicodeEncodeError:
                        continue
                else:                    
                    textChi = pytesseract.image_to_string(Image.open(fullpath),lang='chi_sim')
                    if delLineSpace(textChi) == '':
                        continue
                    text = '��' + fullpath + '�������ġ�\n' + delLineSpace(textChi) + '\n\n'
                    try:
                        fp.write(text)
                    except UnicodeEncodeError:
                        continue
                    textEng = pytesseract.image_to_string(Image.open(fullpath),lang='eng')
                    if delLineSpace(textEng) == '':
                        continue
                    text = '��' + fullpath + '����Ӣ�ġ�\n' + delLineSpace(textEng) + '\n\n'
                    try:
                        fp.write(text)
                    except UnicodeEncodeError:
                        continue
root.destroy()
root.mainloop()
fp.close()
win32api.ShellExecute(0, 'open', 'notepad.exe', u'ͼ��ʶ����.txt','',1)


