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
@file: 1.mutiprocessing.py
@time: 2018/1/24 18:30
"""
import os
import multiprocessing
def info(title):
    print(title)
    print('father ppid',os.getppid())
    print('self pid',os.getpid())
    print("-----")

if __name__=='__main__':

    p1=multiprocessing.Process(target=info,args=("abc1",))#进程需要添加start（）启动
    p2=multiprocessing.Process(target=info,args=("abc2",))#进程需要添加start（）启动
    p3=multiprocessing.Process(target=info,args=("abc3",))#进程需要添加start（）启动
    p1.start()
    p2.start()
    p3.start()
    p1.join()#join 在这里为了等待所有进程都结束
    p1.join()
    p1.join()
    print("all over")

    '''
#进程轮流干活
p1.start()
p1.join()#父亲线程必须等待子进程干完活才能执行后面的代码。如果不用join最后执行父进程
p2.start()
p2.join()#父亲线程必须等待子进程干完活才能执行后面的代码。如果不用join最后执行父进程
p3.start()
p3.join()#父亲线程必须等待子进程干完活才能执行后面的代码。如果不用join最后执行父进程
print("hello!~~")
'''