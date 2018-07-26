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
@file: 5.singnal.py
@time: 2018/1/24 18:15
"""
#信号
import subprocess
import signal# 执行一个指令被意外终端 返回一个信号
#signal 只能在命令窗口抓取到，
def itout(signum,frame):#函数挂接信号
    print("signal is end")#

signal.signal(signal.SIGILL,itout)#意外终端启动函数
pingP=subprocess.Popen(args=['ping www.baidu.com'],shell=True)
pingP.wait()
print(pingP.pid)
print(pingP.returncode)


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass


