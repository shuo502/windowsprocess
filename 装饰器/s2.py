import time
def timer(func):  #其实就是返回一个返回一个内存地址，返回的是test3的地址
    def test3(*args,**kwargs):  #这里传入非固定参数，表示可有可无，可单个，可多个
        start_time = time.time()
        x = func(*args,**kwargs) #这里表示是被装饰的函数传递的参数
        end_time = time.time()
        print(end_time - start_time)
        # print('x表示被装饰函数的返回值：',x)
        return 'x表示被装饰函数的返回值：%s'%x
    return test3    #这里是将test3的内存地址赋给test1，然后执行的是test3
  #因此这里实际上执行的是test3，但是在这里面它执行了test1而已
# 最终实现的效果
@timer   # 相当于test1 = timer(test1)
def test1():  #这里没有传入参数，因此在装饰器中使用了非固定参数解决
    time.sleep(2)
    x = 1
    print('in the test1')
    return x

@timer
def test2(name,age):  #这里传入了两个参数
    time.sleep(1)
    print('in the test2 ：',name,age)
    return "cc"
# 这就是装饰器，没有修改运行test1函数，只是自己写了一个函数然后使用装饰器装饰后使用
print(test1())
print(test2("aa","bb"))
# test2(1,2)