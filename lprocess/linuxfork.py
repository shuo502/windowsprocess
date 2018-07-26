#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: os.fork()
@license: Apache Licence 
@contact: shuo502@163.com
@author: ‘yo‘
@site: http://github.com/shuo502
@software: PyCharm
@file: processfok.py
@time: 2018/1/24 17:38
"""
#linux 下os模块才有 fork
import os
pid=os.fork()#创建一个子进程 在子进程里面 PID =0 #复制这个进程
print("abc")
print("ccc")
print(pid)
if pid==0:
    print('pid==0','i am son 子进程')
else:
    print("pid!=0", 'i am ,father 父进程')
#fork进程拷贝代码拷贝fork 以后的代码
#os.fork=返回两个值，
#任何子进程都有一个编号，父进程和子进程的编号
#




def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass


