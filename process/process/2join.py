import  os
import multiprocessing
import time

def info(title):
    print(title)
    time.sleep(2)
    print(__name__)
    print("father ppid",os.getppid())
    print("self pid", os.getpid())
    print("-----------")

if  __name__=="__main__":
    p1 =multiprocessing.Process(target=info,args=("A1",))
    p2 = multiprocessing.Process(target=info, args=("A2",))
    p3 = multiprocessing.Process(target=info, args=("A3",))
    p1.start() #并发干活
    p2.start()
    p3.start()
    #p1.join()
    #p2.join()
    #p3.join()
    print("all over")

    '''
       #进程轮流干活
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()

    '''
