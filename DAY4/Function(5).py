# Author: Li tianyang

#参数组 （非固定参数）
'''def test(x,y):
    print(x)
    print(y)

test(1,2,3)'''

'''若实参数目不固定，此时形参该如何定义？？'''

# * >>>>接收参数（必须是位置参数）数目不固定  就写成 *args 规范就是规范!
def test(*args):
    print(args)


#test(1,2,3,4,5,6)          #输出到一个元组里
test(*[1,2,3,4,5,6])       #输出到一个元组里

# *args：接收N个位置参数，转换成元组的形式
def test1(x,*args):
    print(x)
    print(args)

test1(1,2,3,4,5,6,7,8)

#把n个关键字参数，转换成字典
def test2(**kwargs):
    print(kwargs)

test2(name='Litianyang',age='永远的18')

#混合使用
def test3(name,**kwargs):
    print(name)
    print(kwargs)
test3('Litianyang',age=18,sex='m')

