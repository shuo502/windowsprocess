import os
#多进程是乱序，并发执行
#多进程加锁，挨个执行，任然是乱序
import multiprocessing
import time
def showdata(lock,i):
    with lock:
        pass
        time.sleep(2)
        print(i)
#进程模拟线程干活
if __name__=='__main__':
    pass
    lock=multiprocessing.RLock()#创建锁

    for num in range(10):
        multiprocessing.Process(target=showdata,args=("1",num)).start()