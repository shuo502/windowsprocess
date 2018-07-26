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
@file: 6queue.py.py
@time: 2018/1/25 10:46
"""
import multiprocessing
queue=multiprocessing.Queue()#队列，可以共享

def func(myq):
    print(id(myq))#查看地址
    # print(myq.put)
    myq.put([1,2,3,4,5])#子进程插入

##
#pipe双向管道，
#queue队列 单向通信，要么子进程插入父进程取出，
#   要么父进程插入，子进程读取。
##

if __name__ == '__main__':
    pass
    print(id(queue))#查看地址
    queue.put(['a','b'])#父进程插入
    p=multiprocessing.Process(target=func,args=(queue,))
    p.start()
    p.join()
    print(queue.get())#父进程取出
    # #如果能成功取出说明父子进程队列可以实现共享

