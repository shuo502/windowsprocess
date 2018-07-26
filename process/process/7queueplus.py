import multiprocessing
import os
queue=multiprocessing.Queue()#队列可以实现共享-单向

def  adddata(queue,i):
    queue.put(i)
    print("put",os.getppid(),os.getpid(),i)

if __name__=="__main__":
    mylist=[]
    for i  in range(10):
        p=multiprocessing.Process(target=adddata,args=(queue,i))
        p.start()
        #print(queue.get())
        mylist.append(queue.get())
    print(mylist)
