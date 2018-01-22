# Author: Li tianyang

import time
def timer(func):   # timer(test1)    func=test1
    def deco():
        start_time=time.time()                #定义了变量没什么卵用
        func()                              #run test1
        stop_time=time.time()
        print("the func run time is %s" %(stop_time-start_time))
    return deco

@timer   #test1=timer(test1)
def test1():
    time.sleep(3)
    print("in the test1")
@timer
def test2():
    time.sleep(3)
    print("in the test2")


test1()
test2()