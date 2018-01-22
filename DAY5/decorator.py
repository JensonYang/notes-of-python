# Author: Li tianyang

# 装饰器：
# 定义：本质是函数，功能：（装饰其他函数）就是为其他函数添加附加功能
# 原则：1.不能修改被装饰的函数的 源代码
#      2.不能修改被装饰的函数的调用方式
# 实现装饰器知识储备：
#                   1.函数即“变量”     解释器只要解释到，内存空间就会分配一块空间
#                   2.高阶函数（能做到不修改被装饰函数源代码的情况下为其添加功能）
#                   3.嵌套函数
#               高阶函数+嵌套函数 = 装饰器

import time

#装饰器
def timmer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print("the func run time is %s" %(stop_time-start_time))
    return warpper()
#函数
@timmer
def test1():
    time.sleep(3)
    print("in the test1")

test1       #有bug