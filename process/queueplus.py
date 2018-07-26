#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: mum
@license: Apache Licence 
@contact: shuo502@163.com
@author: ‘yo‘
@site: http://github.com/shuo502
@software: PyCharm
@file: queueplus.py
@time: 2018/1/25 11:00
"""
import multiprocessing
import os
queue=multiprocessing.Queue()#队列实现共享单向

def adddata(queue,i):
    queue.put(i)
    print("put",os.getppid(),os.getpid(),i)


if __name__ == '__main__':
    pass
    mylist=[]
    for i in range(10):
        p=multiprocessing.Process(target=adddata,args=(queue,i))
        p.start()
        print(queue.get())
        mylist.append(queue.get())#收集进程数据
    print(mylist)