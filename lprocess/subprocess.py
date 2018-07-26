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
@file: subprocess.py.py
@time: 2018/1/24 18:08
"""
#date 代表日期，shell 当作外部指令
#subprocess 作用  执行一个指令，传一个指令返回一个结果
import subprocess
pingP=subprocess.Popen(args=['date'],shell=True)
pingP.wait()#等待
print(pingP.pid)#打印编号
print(pingP.returncode)#返回一个值



def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass


