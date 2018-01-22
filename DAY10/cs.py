# Author: Li tianyang


class Role(object):
    n=123                                   #类变量的
    name = "我是类name"
    def __init__(self, name, role, weapon, life_value=100, money=15000):    #传参数，记住这种格式
        #构造函数
        #在实例化时做一些类的初始化的工作。
        self.name = name                    #实例变量（静态属性）， 作用域就是实例本身

        self.role = role

        self.weapon = weapon

        self.life_value = life_value

        self.money = money

    def shot(self):                          #类的方法，功能（动态属性）
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("%s just bought %s" %(self.name,gun_name) )


r1 = Role('Alex', 'police', 'AK47')     #实例化(初始化一个类，相当于造了一个对象)

r2 = Role('Jack', 'terrorist', 'B22')   #生成一个角色

r1.buy_gun('AK47')   #r1中并没有buy_gun这个函数，实际上Role.buy_gun(r1)，
                     # 把r1传进去，告诉Role谁在调用 ，上述函数中每一个都写了一个self，就是为了接收r1.

print(Role.n)
print(r1.n, r1.name)    #问题就来了？？？ 为什么r1可以调用类变量n????
                        #--------------------------------------> 先搜索实例变量，在搜索类变量
r1.n = "改类变量"
print(r1.n)             #r1：本质上是在r1的内存中加了一个 n = "改类变量"，也没有改类变量
print(r2.n)             #r2：没有改变类变量