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
    info('hello')
    #多进程模块
    p=multiprocessing.Process(target=info,args=("abc",))#进程需要添加start（）启动
    p.start()
    p.join()#父亲线程必须等待子进程干完活才能执行后面的代码。如果不用join最后执行父进程
    print("hello!~~")