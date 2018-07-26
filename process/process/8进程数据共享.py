
import multiprocessing

def  func(num):
    num.value=10.78

if  __name__=="__main__":
    num=multiprocessing.Value("d",10.0) # d数据,多个进程之间共享
    print(num.value)

    p=multiprocessing.Process(target=func,args=(num,))
    p.start()
    p.join()

    print(num.value)