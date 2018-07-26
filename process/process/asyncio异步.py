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
@file: asyncio异步.py
@time: 2018/1/30 17:31
"""
import asyncio

import time
def job(t):
    print('start job',t)

    asyncio.sleep(t)
    print('job',t,'takes',t,'s')
def main(loop):
    tasks=[loop.create_task(job(t)) for t in range(1,3) ]
    asyncio.wait(tasks)
# async def job(t):
#     print('start job',t)
#     await asyncio.sleep(t)
#     print('job',t,'takes',t,'s')
# async def main(loop):
#     tasks=[loop.create_task(job(t)) for t in range(1,3) ]
#     await asyncio.wait(tasks)

t1=time.time()
loop=asyncio.get_event_loop()
loop.run_until_complete(main(loop))
print('async total time:',time.time()-t1)


if __name__ == '__main__':
    pass


