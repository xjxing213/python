# coding=UTF-8
import zipfile,os


path = r'C:\Users\admin\Desktop\19套BSC最新License文件20180831'
##list = os.listdir(path) #列出文件夹下所有的目录与文件
##for i in range(0,len(list)):
##    fpath = os.path.join(path,list[i])
##    if os.path.splitext(fpath)[1].lower() =='.dat':
##        with open(fpath, 'r', encoding='utf-8') as f:
##            cont = f.read()
##            for esn in dic:
##                if cont.find(esn) != -1:
##                    f.close()
##                    lpath = path+'\cbsclicense.dat'
##                    os.mkdir(path + '\\'+ dic[esn])
##                    os.rename(fpath,lpath)
##                    shutil.move(lpath, path + '\\'+ dic[esn] + '\cbsclicense.dat')
##                    city = dic[esn][0:3] + 'License.zip'
##                    break

city = '深圳License.zip'
zipfilepath = os.path.join(path,city)
mypath = path.split('\\')[-1]
print(mypath)
