# Author: Li tianyang

def test1():
    print('in the test1')
    return 0    # 结束标识，终止函数
def test2():
    print('in the test1')

def test3():
    print('in the test1')
    return 1, 'hello', ['alex','wupeiqi'],{'name','alex'}    # C语言当中只能返回一个值，python可以多个（但是本质上还是返回一个,返回的是一个元组）


x=test1()
y=test2()
z=test3()
print(x)
print(y)
print(z)

#为什么要有返回值：最重要的是要一个执行结果