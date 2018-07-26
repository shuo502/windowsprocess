import multiprocessing
queue=multiprocessing.Queue()#队列可以实现共享

def func(myq):
    print(id(myq)) #查看地址
    #myq.put([1,2,3,4,5]) #子进程插入
    print(myq.get())

if __name__=="__main__":
    print(id(queue)) #查看地址
    queue.put([1, 2, 3, 4, 5])
    p=multiprocessing.Process(target=func,args=(queue,))
    p.start()
    p.join()
    #print(queue.get()) #父亲进程取出

#队列，单项通信，
#父进程插入，子进程读取
#子进程写入，父进程读取