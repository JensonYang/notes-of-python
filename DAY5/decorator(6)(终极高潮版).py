# Author: Li tianyang

import time
user,passwd = 'Litianyang',"132465.."
def auth(auth_type):
    print("auth func:", auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            print("wrapper func args:", *args, **kwargs)
            if auth_type == "local":
                username = input("Username:").strip()
                password = input("Password:").strip()
                if user == username and passwd == password:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    return func(*args, **kwargs)

                else:
                    exit("\033[31;1mInvalid username or password\033[0m")
            elif auth_type == "ldap":
                print("搞什么ldap，不会。")


        return wrapper
    return outer_wrapper

def index():   #首页
    print("welcome to index page")
@auth(auth_type="local")
def home():    #主页
    print("welcome to home page")
    return "from home"
@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs page")

index()
print(home())   #调用home时，相当于调用的是wrapper,wrapper中并没与返回值的啊！！！
bbs()
