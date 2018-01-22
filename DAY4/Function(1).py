# Author: Li tianyang

#定义函数
def func1():
    """texting1"""
    print('in the func1')
    return 0

#定义过程
def func2():
    '''testing2'''
    print('in the func2')    #过程就是没有返回值的函数
                             #python中也隐式的给过程定义了返回值none

#调用
x=func1()
y=func2()

print('from func1 return is %d' %x)    #没有逗号！！
print('from func2 return is %s' %y)




