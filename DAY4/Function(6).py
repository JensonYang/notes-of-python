# Author: Li tianyang


#函数必须在调用之前，因为程序执行是从上到下
def test4(name,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("test4")
def logger(source):
    print("from %s" % source)
test4('Litianyang',age=34,sex='m',hobby='tesla')