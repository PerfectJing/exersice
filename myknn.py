from numpy import *
import operator
from os import listdir

def knn(k,testdata,traindata,labels):
    traindatasize=traindata.shape[0]#获得训练数据的行数
    #可能训与测维数不一样，扩展测试数据的行维数与训一样,再算差
    dif=tile(testdata,(traindatasize,1))-traindata#1列不变
    sqdif=dif**2#平方
    sumsqdif=sqdif.sum(axis=1)#1是每一行的和，axis=0每一列的和
    distance=sumsqdif**0.5#开方
    sortdistance=distance.argsort()#返回的是从小到大索引
    #选取距离最小的k个点
    count={}#设置一个空字典
    for i in range(0,k):
        vote=labels[sortdistance[i]]#属于的类别
         #统计哪个类别多，get()
        count[vote]=count.get(vote,0)+1
        #取类别最大的，get得到的是【值，次数】按第二个参数（次数）排从大到小排
    sortcount=sorted(count.items(),key=operator.itemgetter(1),reverse=True)
    #取出排序后第一个值中排在前面的第一个元素值
    return sortcount[0][0]
#图片处理,转为文本
from PIL import Image
im=Image.open("rice.png")
fh=open("rice.txt","a")
width=im.size[0]
height=im.size[1]
for i in range(0,width):
    for j in range(0,height):
        col=im.getpixel((i,j))#获取像素
        #colall=col[0]+col[1]+col[2]
        if(col==0):
            #黑色写入1
            fh.write("1")
        else:
            fh.write("0")
    fh.write("\n")
fh.close()

#加载数据,转化为数组
def datatoarray(fname):
    arr=[]#初始为空
    fh=open(fname)#打开文本
    for i in range(0,32):
        thisline=fh.readline()
        for j in range(0,32):
            arr.append(int(thisline[j]))#加载到数组中
    return arr
arr1=datatoarray("testdata/0_0.txt")
#建立一个函数返回文件的前缀
def seplabel(fname):
    #先将文件名以点分割，取第一个
    filestr=fname.split(".")[0]
    #再将前一部分以下划线分割，取第一个
    label=int(filestr.split("_")[0])
    return label
#建立训练数据

def traindata():
    labels=[]
    #listdir得到一个文件夹下所有的文件名
    trainfiles=listdir("traindata")#得到训练目录下的所有文件
    num=len(trainfiles)
    #每一行存贮一个文件，长度是1024
    #用一个数组存储所有训练数据，行是文件总数，列是1024（32*32）
    trainarr=zeros((num,1024))
    #将内容加载到trainarr
    for i in range(0,num):
        thisfname=trainfiles[i]
        #当前类别
        thislabel=seplabel(thisfname)
        labels.append(thislabel)
        trainarr[i,:]=datatoarray("traindata/"+thisfname)
    return trainarr,labels
#用测试数据调用knn算法去测试
def datatest():
    trainarr,labels=traindata()
    testlist=listdir("testdata")
    tnum=len(testlist)
    for i in range(0,tnum):
        thistestfile=testlist[i]
        testarr=datatoarray("testdata/"+thistestfile)
        rknn=knn(3,testarr,trainarr,labels)
        print(rknn)
    #datatest()
#抽取某一测试文件
trainarr,labels=traindata()
thistestfile="6_30.txt"
testarr=datatoarray("testdata/"+thistestfile)
rknn=knn(3,testarr,trainarr,labels)
print(rknn)





