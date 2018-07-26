#进程之间的管道通信 进程通信 ，一个发一个收
# a,b=(1,2)
# print(a,b) a=1,b=2
import multiprocessing
import os
def func(conn):#conn管道类型
    pass
    conn.send(['a','b','c','d','e'])#发送的数据
    print(conn.recv())#收到的数据
    conn.close()##关闭

if __name__=="__main__":
    conn_a,conn_b=multiprocessing.Pipe()#创建一个管道两个数据口
    # print(id(conn_a),id(conn_b))
    # print(type(id(conn_a)),type(id(conn_b)))
    p=multiprocessing.Process(target=func,args=(conn_a,))
    p.start()
    conn_b.send([1,2,3,4,5,6,7])
    print(conn_b.recv())
    p.join()