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
@file: 进程数据共享.py
@time: 2018/1/25 11:05
"""

import multiprocessing
def func(num):
    num.value=10.9

if __name__ == '__main__':
    num=multiprocessing.Value("d",0.0)#d 数据，s 字符串#多个进程直接共享数据
    p=multiprocessing.Process(target=func,args=(num,))
    p.start()
    p.join()


    print(num.value)

    pass


