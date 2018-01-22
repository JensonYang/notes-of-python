# Author: Li tianyang


# 列表 字典 类都是可以在函数中修改的
# 字符串和整数是不可以修改的
names = ['Litianyang','Jack','Rain']
def change_name():
   names[0] = '金角大王'
   print("inside func",names)

change_name()
print(names)