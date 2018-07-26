
import  os
import multiprocessing

def info(title):
    print(title)
    print(__name__)
    print("father ppid",os.getppid())
    print("self pid", os.getpid())
    print("-----------")

if  __name__=="__main__":
    info("hello")

    #多进程
    p=multiprocessing.Process(target=info,args=("gaoqinghua",))
    p.start()
    p.join()#父亲进程必须等待子进程干完活，执行后续代码
    print("hello  hechengcheng")