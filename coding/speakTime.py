import time,pygame,datetime
from aip import AipSpeech


def mythread(timeout,func):
    tHandle = threading.Thread(target=func)
    tHandle.setDaemon(True) 
    tHandle.start()
    tHandle.join(timeout) 
    print 'timeout'

def playMp3:
    file='myvoice.mp3'
    pygame.mixer.init()
    print("播放音乐")
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    time.sleep(10)
    pygame.mixer.music.stop()

    
while True:
##    minutes=int(str(datetime.datetime.now())[15:16])
##    print(minutes)
    now=str(datetime.datetime.now())[:19]
    APP_ID = '1468'
    API_KEY = 'HbB9spO0atlPBX'
    SECRET_KEY = 'SIXU6axXOZk2XgG9u' 
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    str1='现在时间是：' + now
    result  = client.synthesis(str1, 'zh', 1, {'vol': 7,'per':0})
         
    #识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('myvoice.mp3', 'wb') as f:
            f.write(result)
    

    time.sleep(15)
