import  os
import multiprocessing
import time
#多进程，并发，乱序并发执行
#多进程加锁，挨个执行，仍然是乱序

def  showdata(lock,i):
    with lock:
        time.sleep(2)
        print(i)


if __name__=="__main__":
    lock=multiprocessing.RLock()#创建锁
    for num in range(2):
        multiprocessing.Process(target=showdata,args=( lock,num)).start()