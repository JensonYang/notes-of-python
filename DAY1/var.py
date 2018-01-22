# Author:Li tianyang
name = "Li tianyang"          # name指向了Li tianyang,name2借助name
name2 = name                  # 指向了Li tianyang，与name没有关系
print("My name is ", name2)

name = "PaoChe ge"

                              #  变量名一定要写其含义

gf_of_oldboy = "Chen rong hua"

                              #  GFOfOldboy  驼峰 Windows经常这样写

                              #  定义常量要大写，python中没有常量的概念
PIE = 5


print(name, name2)