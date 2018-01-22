# Author: Li tianyang

# 生成器是假如要用第1000个元素，就必须从第一个开始循环到第1000个，一次步子不能迈得太大！
# 生成器只有在调用时才会产生相应的数据，只记录当前位置
# 列表生成式是一次全部准备好，可以直接调用任何一个元素。

# 我们正确的方法是使用for循环，因为generator也是可迭代对象

g = (x*x for x in range(10))

for i in g:
    print(i)

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b, a+b    # 注意这里的赋值语句 ！！！！
                        #  相当于有个中间变量t = (b,a+b) a = t[]
        n = n +1
    return 'done'

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        #print(b)
        yield b          #如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
        a,b = b, a+b
        n = n +1
    return 'done'

fib_gen = fib(10)     #很自由 想进想出 并不用必须等着函数全部执行完毕
                       # 非常牛逼
print(fib_gen.__next__())
print(fib_gen.__next__())
print(fib_gen.__next__())
print(fib_gen.__next__())
print(fib_gen.__next__())
# for i in fib_gen:
#      print(i)




