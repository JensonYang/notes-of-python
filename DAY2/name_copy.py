# Author:Li tianyang
#----------------------------------------------------
        #浅copy 经常用作联合账号(虽然是不存在的)
#----------------------------------------------------
names = ["Zhangsan", "Lisi", "Wangwu",["Alex", "Jenson"], "Litianyang", "Chenronghua"]

name2 = names.copy()    # ["Alex", "Jenson"] 实则在names中存放的本质是指针，即存储方式师这个列表的地址
                        # 浅copy只是copy了地址
print(names)
print(name2)

names[2] = "王五"       # 这在name2中却没有修改
names[3][0] = "赵茜"    # 列表嵌套结构修改，但此时copy的name2却改变了？？？

print(names)
print(name2)           # 此copy是浅copy,只是第一个列表的引用

#name2 = names 此时是用同一块内存 因此也不行

import copy
name2 = copy.deepcopy(names)  # deepcopy 完全clone
print(name2)
print(names[0:-1:2])        #步长切片
print(names[::2])
#range(1,10,2)
for i in names:           # 列表循环
    print(i)


