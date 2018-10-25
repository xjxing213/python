# -*- coding:utf-8 -*-
import tkinter
 
root = tkinter.Tk()
root.title('OCR图片识别')        #窗口标题
root.resizable(False, False)    #固定窗口大小
windowWidth = 500               #获得当前窗口宽
windowHeight = 200              #获得当前窗口高
screenWidth,screenHeight = root.maxsize()     #获得屏幕宽和高
geometryParam = '%dx%d+%d+%d'%(windowWidth, windowHeight, (screenWidth-windowWidth)/2, (screenHeight - windowHeight)/2)
root.geometry(geometryParam)    #设置窗口大小及偏移坐标
root.wm_attributes('-topmost',1)#窗口置顶
 
#label文本
label_text = tkinter.Label(root, text = '文本');
label_text.pack();
root.mainloop()

