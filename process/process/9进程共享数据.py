
import multiprocessing

def  func(num):
    num[2]=9999

if  __name__=="__main__":
    num=multiprocessing.Array("i",[1,2,3,4,5])# d数据,多个进程之间共享
    print(num[:])

    p=multiprocessing.Process(target=func,args=(num,))
    p.start() #进程之间数据共享
    p.join()

    print(num[:])