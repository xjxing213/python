# -*- coding: cp936 -*-
import os
import linecache
import datetime

ypArr=[]
pointSumArr=[]
fileName=[]
#pointArr=[]
fileName_ypPd=[]

#�������ͳ��

localPath=os.getcwd()
for dirpath,dirnames,filenames in os.walk(localPath):
    for file in filenames:
            fullpath=os.path.join(dirpath,file)
            #print('fullpath=' + fullpath)
            #��ȡ�ļ���
            
            fn=fullpath[fullpath.rfind('\\',)+1:fullpath.rfind('-',)]
            #print('fn=' + fn)
            rfile=linecache.getlines(fullpath)
            sum=1

            n=0
            s=rfile[n]
            s=s.rstrip('\n')
            while s == '':    #�����ͷΪ���У��������ȡ��һ�У�ֱ��������Ϊֹ
                n=n+1
                s=rfile[n]
                s=s.rstrip('\n')
            if fullpath.find('������Ƶtxt')>0 or fullpath.find('ɾ����Ƶtxt')>0:                
                if fullpath.find('������Ƶtxt')>0:
                    s1_yp=s.split('=')[2].split(',')[0]
                    #print(s1_yp)
                    pre='����-'
                elif fullpath.find('ɾ����Ƶtxt')>0:
                    s1_yp=s.split('=')[2].split(';')[0]
                    #print(s1_yp)
                    pre='ɾ��-'
                else:
                    print('�����·���ǲ��Ǵ���߹��')

                for index in range(n+1,len(rfile)):
                    s=rfile[index]
                    #print(s)
                    s=s.rstrip('\n')
                    #print(s)
                    if s!='':
                        if fullpath.find('������Ƶtxt')>0:
                            s_yp=s.split('=')[2].split(',')[0]
                            #print(s_yp)
                            pre='add_'
                        elif fullpath.find('ɾ����Ƶtxt')>0:
                            s_yp=s.split('=')[2].split(';')[0]
                            pre='del_'
                        else:
                            print('�����·���ǲ��Ǵ���߹��')

                    if s1_yp==s_yp:
                        sum=sum+1
                    else:     
                        string=pre + fn + '_point:' + s1_yp
                        #print(string)
                        #pointArr.append(s1_yp)
                        fileName_ypPd.append(string)
                        pointSumArr.append(str(sum))        
                        s1_yp=s_yp
                        sum=1
                else:
                    string=pre + fn + '_point:' + s1_yp
                    #pointArr.append(s1_yp)
                    fileName_ypPd.append(string)
                    pointSumArr.append(str(sum))

dict = {} #����һ�����ֵ�
for l in fileName_ypPd:
    #print(l)
    if l in dict:
        dict[l] += 1
    else:
        dict[l] = 1
        
thisFileName = 'ͳ�ƽ��' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.txt'
fp=open(thisFileName, 'a+')

print(dict)
print('\n')

#����ת���������б�[('a',1),('b',2)]
mylist = sorted(dict.iteritems(),key = lambda asd:asd[0], reverse = False)

#print(dic[0])
#print(dic[0][0])
#print(dic[0][1])


markNum = 0
for listValue in mylist:
    #print(key + ' sum��' + str(dict[key]))
    #del_svr1_point:500 sum��22645
    AddDel_svr_point_sum = listValue[0] + ' sum��' + str(listValue[1]) + '\n'
    
    if markNum == 0:
        theFirstSvr = listValue[0].split('_')[1] #���θ�ֵ������ѭ��ִֻ��һ�α����
        #print(theFirstSvr)
        markNum = 1
    
    if markNum != 0:
        theCurrentSvr = listValue[0].split('_')[1] #��ǰsvr����һ�����⣩
        #print(theCurrentSvr)
        if theCurrentSvr !=  theFirstSvr:
            AddDel_svr_point_sum = '-------------------------------\n' + AddDel_svr_point_sum
            theFirstSvr = theCurrentSvr
            markNum = 1
        
    fp.write(AddDel_svr_point_sum)

fp.close()





    
        






