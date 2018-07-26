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
@file: 11.pool.py
@time: 2018/1/30 16:42
"""
import multiprocessing as mp
#进程池
def func(x):
    return x*x

def multicore():
    pool=mp.Pool()
    res=pool.map(func,range(10))
    print(res)
    res=pool.apply_async(func,(2,))
    print(res.get())
    mulitres=[pool.apply_async(func,(i,))for i in range(10)]
    print([res.get() for res in mulitres])



if __name__ == '__main__':
    pass
    multicore()


