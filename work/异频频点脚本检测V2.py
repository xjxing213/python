# -*- coding: cp936 -*-
import os
import linecache
import datetime

ypArr=[]
pointSumArr=[]
fileName=[]
#pointArr=[]
fileName_ypPd=[]

#排序后再统计

localPath=os.getcwd()
for dirpath,dirnames,filenames in os.walk(localPath):
    for file in filenames:
            fullpath=os.path.join(dirpath,file)
            #print('fullpath=' + fullpath)
            #获取文件名
            
            fn=fullpath[fullpath.rfind('\\',)+1:fullpath.rfind('-',)]
            #print('fn=' + fn)
            rfile=linecache.getlines(fullpath)
            sum=1

            n=0
            s=rfile[n]
            s=s.rstrip('\n')
            while s == '':    #如果开头为空行，则继续读取下一行，直到有内容为止
                n=n+1
                s=rfile[n]
                s=s.rstrip('\n')
            if fullpath.find('新增异频txt')>0 or fullpath.find('删除异频txt')>0:                
                if fullpath.find('新增异频txt')>0:
                    s1_yp=s.split('=')[2].split(',')[0]
                    #print(s1_yp)
                    pre='新增-'
                elif fullpath.find('删除异频txt')>0:
                    s1_yp=s.split('=')[2].split(';')[0]
                    #print(s1_yp)
                    pre='删除-'
                else:
                    print('你给得路径是不是错了吖！')

                for index in range(n+1,len(rfile)):
                    s=rfile[index]
                    #print(s)
                    s=s.rstrip('\n')
                    #print(s)
                    if s!='':
                        if fullpath.find('新增异频txt')>0:
                            s_yp=s.split('=')[2].split(',')[0]
                            #print(s_yp)
                            pre='add_'
                        elif fullpath.find('删除异频txt')>0:
                            s_yp=s.split('=')[2].split(';')[0]
                            pre='del_'
                        else:
                            print('你给得路径是不是错了吖！')

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

dict = {} #创建一个空字典
for l in fileName_ypPd:
    #print(l)
    if l in dict:
        dict[l] += 1
    else:
        dict[l] = 1
        
thisFileName = '统计结果' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.txt'
fp=open(thisFileName, 'a+')

print(dict)
print('\n')

#排序转换后变成了列表[('a',1),('b',2)]
mylist = sorted(dict.iteritems(),key = lambda asd:asd[0], reverse = False)

#print(dic[0])
#print(dic[0][0])
#print(dic[0][1])


markNum = 0
for listValue in mylist:
    #print(key + ' sum：' + str(dict[key]))
    #del_svr1_point:500 sum：22645
    AddDel_svr_point_sum = listValue[0] + ' sum：' + str(listValue[1]) + '\n'
    
    if markNum == 0:
        theFirstSvr = listValue[0].split('_')[1] #初次赋值，整个循环只执行一次本语块
        #print(theFirstSvr)
        markNum = 1
    
    if markNum != 0:
        theCurrentSvr = listValue[0].split('_')[1] #当前svr（第一个除外）
        #print(theCurrentSvr)
        if theCurrentSvr !=  theFirstSvr:
            AddDel_svr_point_sum = '-------------------------------\n' + AddDel_svr_point_sum
            theFirstSvr = theCurrentSvr
            markNum = 1
        
    fp.write(AddDel_svr_point_sum)

fp.close()





    
        






