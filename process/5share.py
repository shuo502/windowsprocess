#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: mum
@license: Apache Licence 
@contact: shuo502@163.com
@author: ‘yo‘
@site: http://e-learning.51cto.com/video/195058
@software: PyCharm
@file: s'cha're.py
@time: 2018/1/24 18:45
"""
import multiprocessing
import time
import os

datalist=[] #全局变量
#全局变量每个东西都会拷贝一便
def adddata():
    global datalist
    datalist.append(1)
    datalist.append(2)
    datalist.append(3)
    print(os.getpid()<datalist)

# def show(mylist):
#     for data in mylist

if __name__ == '__main__':
    pass
    p=multiprocessing.Process(target=adddata(),args=())
    p.start()

    datalist.append("a")
    datalist.append("b")
    datalist.append("c")


