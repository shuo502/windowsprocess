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
@file: 12.Value 共享内存.py
@time: 2018/1/30 16:50
"""


"""Type code
C Type  C语言类型
Python Type  py类型
Minimum size in bytes  数据占用字节
Notes  其他
--------
'b'
signed char
int
1
 -----
'B'
unsigned char
int
1
 -----
'u'
Py_UNICODE
Unicode character
2
(1)
-----
'h'
signed short
int
2
 -----
'H'
unsigned short
int
2
 -----
'i'
signed int
int
2
 -----
'I'
unsigned int
int
2
 -----
'l'
signed long
int
4
 -----
'L'
unsigned long
int
4
 -----
'q'
signed long long
int
8
(2)
-----
'Q'
unsigned long long
int
8
-----
(2)
'f'
float
float
4
 -----
'd'
double
float
8
 """
import multiprocessing as mp


value=mp.Value('d',1)
array=mp.Array('i',[1,2,3])#一维列表

import time
def job(v,num,l):
    l.acquire()#上锁
    for _ in range(10):
        time.sleep(0.1)
        v.value+=num#使用共享内存
        print(v.value)
    l.relese()#解锁

def multicore():
    l=mp.Lock()#锁
    v=mp.Value('i',0)#共享内存i 整型，初始值0
    p1=mp.Process(target=job,args=(v,1,l))
    p2=mp.Process(target=job,args=(v,3,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    pass


