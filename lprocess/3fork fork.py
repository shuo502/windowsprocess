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
@file: 3fork fork.py
@time: 2018/1/24 17:58
"""
#轻量级多进程
#ppid父进程，pid 子进程
import os

pid=os.fork()
if pid ==0:
    print("a",os.getpid(),os.get.ppid())
else:
    print("b",os.getpid(),os.get.ppid())

pid=os.fork()
if pid ==0:
    print("d",os.getpid(),os.get.ppid())
else:
    print("e",os.getpid(),os.get.ppid())

#linux 查看所有进程   ps -aux  win查看进程tasklist





def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass


