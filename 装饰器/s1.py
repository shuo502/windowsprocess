import time
def test1():
    time.sleep(2)
    print('in the test1')
def test2():
    time.sleep(2)
    print('in the test2')

#如果要装饰test1或test2，就要做下面的操作

def timer(func): #其实就是返回一个返回一个内存地址，返回的是test3的地址
    def test3():
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)
    return test3 #这里是将test3的内存地址赋给test1，然后执行的是test3

#在这里你执行test1实际上是执行了test3，但是发现，我并没有修改test1
#的调用方式，但是输出结果却是真正的对test1原有的功能做了添加和优化
#test1()
timer(test1())