# Author: Li tianyang

#继承的过程，就是从一般到特殊的过程。

# class People:经典类
class People(object): #新式类 :多继承的方式变了 （主要就是继承上的区别）
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print("%s is eating ..." % self.name)

    def talk(self):
        print("%s is taking... " % self.name)

    def sleep(self):
        print("%s is sleeping.. " % self.name)

class Relation(object):
    def makefriends(self,obj):          # obj已经时一个对象
        print("%s is making friends with %s" %(self.name,obj.name))         # 此处要理解一下！！！！！！！！！！！！！


class Man(People,Relation):                                       # 此时已经继承了
    def __init__(self,name,age,money):                    #重构，父类所有的参数都要写一遍
        # 经典类方法：People.__init__(self,name,age)      #用一下，把自己传给他

        # 新式类方法>>>>>>>>>>>>>>>
        super(Man,self).__init__(name,age)                #  这里没有出现父类People,若有很多子类重构的话，当父类修改时，
                                                           #  第一种方法重构需要修改许多父类，很麻烦。多继承的话，最好还是用super！！
                                                            #>>>>>>>>>>>>>super的作用就是让子类按照从左到右的顺序继承父类的构造函数，直到找到第一个
        self.money = money
        print("%s 一出生就有%s钱"%(  self.name,self.money  ))

    def piao(self):
        print("%s is piaoing.....20s....done"% self.name)

    def gamble(self):
        print("%s is gamble...." % self.name)

    def sleep(self):                    # 要给父类增加功能:先实现父类功能,再增加子类功能
        People.sleep(self)              # 为什么此处要加self？？>>>>>>>>>>> 执行父类的方法把自己传进去
        print("man is sleeping")

class Woman(People,Relation):
    def get_brith(self):
        print("%s is born a baby..."% self.name)

man1 = Man("Li tianyang", "23","500000")      # 子类要传参数，若此时子类当中没有构造方法，那就只能寻找父类的构造方法。
                                              # 其中，若两个父类均有构造方法的话，执行顺序按照从左到右进行,此时若第一个有构造函数，就不会执行到第二个父类。
                                              # 找到第一个就停下来
                                              # 最后，若父类当中没有构造方法，那就只执行有构造方法的那个父类。
# man1.eat()
# man1.piao()
# man1.sleep()
woman1 = Woman("XXX","23")
# woman1.get_brith()
# woman1.piao()                     子类之间一定不能调用

man1.makefriends(woman1)


