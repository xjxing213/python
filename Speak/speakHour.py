import time,datetime
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
while True:
    minutes=int(str(datetime.datetime.now())[15:16])
    print str(datetime.datetime.now())[11:19]
    #每10分钟报时一次
    if minutes == 0:
        now=str(datetime.datetime.now())[11:19]
        str1=u'现在时间是：' + now
        speaker.Speak(str1)
        time.sleep(35)
    time.sleep(30)
