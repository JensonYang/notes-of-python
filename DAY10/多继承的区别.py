# Author: Li tianyang

class A:
    def __init__(self):
        print("A"

class B(A):
    def __init__(self):
        print("B")

class C(A):
    def __init__(self):
        print("C")

class D(B,C):
    def __init__(self):
        pass


obj = D()

# 子类D() 寻找父类构造的顺序是 B<C<A
# 这里有个问题：按照逻辑来说，若B中没有构造函数，A中有构造函数，那么B是继承了A的，为什么不是直接继承A呢？？
# 由此 产生了 两种不同的继承策略：
#                              1) 按照深度优先      >>>>经典类
#                              1) 按照广度优先      >>>>新式类
#                       py2 经典类是按深度优先来继承的，新式类是按广度优先来继承
#                       py3 经典类和新式类都是统一按照广度优先来继承的