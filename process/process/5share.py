import multiprocessing
import time
import os

datalist=[] #全局变量

def adddata():
    global datalist
    datalist.append(1)
    datalist.append(2)
    datalist.append(3)
    print(os.getpid(),datalist)




if __name__=="__main__":

    p=multiprocessing.Process(target=adddata,args=())
    p.start()


    datalist.append("a")
    datalist.append("b")
    datalist.append("c")
    print(os.getpid(),datalist)

