# Author: Li tianyang

# 高阶函数：1.把一个函数名当做实参传给另外一个函数
#         2.返回值中包含函数名

# 1.把一个函数名当做实参传给另外一个函数
# import time
# def bar():
#     time.sleep(2)
#     print("in the bar")
#
# def test1(func):
#     start_time=time.time()
#     func()          #run bar
#     stop_time=time.time()
#     print("the func run time is %s" %(stop_time-start_time))
# #bar()
# test1(bar)         #此处调用方式却改变了！
'''
 func = bar       此处就是相当于变量，x=1，x=y,xy同时指向了1
 func()
'''
# 2.返回值中包含函数名

def bar1():
     time.sleep(3)
     print("in the bar1")
def test2(func):
    print(func)
    return func

#print(test2(bar1))   #有内存地址 意味着加上（）就能运行
#test2(bar1())若这样写，不符合高阶函数的定义，这是bar1函数的返回值
t=test2(bar1)
t()   #t此时获取了bar1的地址，则加上小括号()>>>>>t() 就相当于运行了bar1
