# Author: Li tianyang
#这种装饰器已经可以满足日常百分之90的需求了
#如何将test2参数传进去
import time
def timer(func):   # timer(test1)    func=test1
    def deco(*args,**kwargs):                 #真正变成了通用的装饰器
        start_time=time.time()                #定义了变量没什么卵用
        func(*args,**kwargs)                  #run test1
        stop_time=time.time()
        print("the func run time is %s" %(stop_time-start_time))
    return deco

@timer   #test1=timer(test1)
def test1():
    time.sleep(3)
    print("in the test1")
@timer  #test2=timer(test2)
def test2(name,age):
    print("test2:",name,age)

test1()
test2("Litianyang",18)