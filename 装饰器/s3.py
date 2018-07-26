import time
user,pawd = 'asd','123' #模拟本地的用户名、密码
def auth(auth_type):
    # print('auth func:',auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            print('wrapper func args kwargs:',*args, **kwargs)
            if auth_type == 'local':
                username = input('username:').strip()
                password = input('password:').strip()
                if user == username and pawd == password:
                    print('wellcome')
                    res = func(*args, **kwargs)
                    return res
                else:
                    exit('用户名或密码错误')
            elif auth_type == 'ldap':
                print('执行ldap里面的验证')
        return wrapper
    return outer_wrapper
def index():
    print('welcome to index page')
#这里传入一个参数是为了理解装饰器传递参数
@auth(auth_type = 'local')  #本地认证方式
def home(name):
    print('welcome to home page')
    return 'from home %s'%name
@auth(auth_type = 'ldap')  #远程认证服务器方式
def bbs():
    print('welcome to bbs page')
# index()
home('name')
# bbs()