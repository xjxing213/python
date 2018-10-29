import cv2 as cv
import numpy as np

def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("height: %s,width: %s,channels: %s"%(height,width,channels))

src=cv.imread(r"C:\Users\Administrator\Desktop\opencv\hzw.jpg")
##cv.namedWindow("image",cv.WINDOW_AUTOSIZE)
##cv.imshow("image",src)
access_pixels(src)
cv.waitKey(0)

cv.destroyAllwindows()

'''
(644, 602, 3)
width: 602,height: 644,channels: 3
'''
