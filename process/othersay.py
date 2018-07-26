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
@file: othersay.py
@time: 2018/1/25 14:17
"""
import multiprocessing

import  os
import time
def func(i):
    # time.sleep(i)
    print("abc:%s" %str(i),os.getpid(),os.getpid())

    pass





if __name__ == '__main__':
    pass
    for i in range(5):
        # i=5-i
        p=multiprocessing.Process(target=func,args=(str(i),))
        p.start()
