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
@file: 2forkvar.py
@time: 2018/1/24 17:54
"""
import os
num=100
pid=os.fork()
if pid==0:
    num+=100
    print("son",num)
else:
    print("father",num)

#fork 会拷贝全局变量，全局变量不是共享的。
#多进程会拷贝fork 代码全局变量，互相是独立的。

def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass


