import cv2 as cv
##摄像头扑捉
def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret,frame = capture.read()
        frame = cv.flip(frame, 1)
        cv.imshow("video",frame)
        c = cv.waitKey(50)
        #按esc停止
        if c == 27:
            break

def get_image_info(image):
    print(type(image)) #
    print(image.shape) #
    print(image.size) #=644*602*3，shape各维度之积
    print(image.dtype) #


src=cv.imread(r"C:\Users\Administrator\Desktop\opencv\hzw.jpg")
cv.namedWindow("image",cv.WINDOW_AUTOSIZE)
cv.imshow("image",src)
get_image_info(src)
video_demo()
cv.waitKey(0)

cv.destroyAllwindows()

'''
<type 'numpy.ndarray'>
(644, 602, 3)
1163064
uint8
'''
