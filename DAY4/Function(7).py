# Author: Li tianyang

#局部变量，全局变量

school = "Northeasten University" #全局变量

def change_name(name):
   # global school        #忘记它        #说明在函数中要修改全局变量，不要写忘记它。
    school = "Mage Linux"
    print("before change:",name,school) #全局变量可以直接访问
    name = "LI TIAN YANG"               #这是一个局部变量，且只是函数中生效。可以理解为这个函数就是这个变量的作用域
    print("after change:",name)


name = "Ltianyang"

change_name(name)
print(name)
print(school)