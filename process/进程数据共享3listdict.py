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

def func(mydict,mylist):
    # num.value=10.9
    # num[2]=999
    mydict["ccb"]="ccc"
    mydict["bbc"]="bbb"
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)



if __name__ == '__main__':
    with multiprocessing.Manager() as MG:
        mydict=MG.dict()
        mydict=MG.list(range(5))
        p=multiprocessing.Process(target=func,args=(mydict,mylist))
        p.start()
        p.join()
        print(mylist)
        print(mydict)