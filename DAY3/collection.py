# Author:Li tianyang
'''集合是一个无序的，不重复的数据组合，它的主要作用如下：
•去重，把一个列表变成集合，就自动去重了
•关系测试，测试两组数据之前的交集、差集、并集等关系'''

#列表变集合
list_1 = [1,4,5,7,3,6,7,9]
list_1 = set(list_1)             #变成了集合
list_2 = set([2,6,0,66,22,8,4])

print(list_1.intersection(list_2))   #取交集 intersection 交叉
print(list_1.union(list_2))          #取并集 union联合的意思
print(list_1.difference(list_2))     #取差集，在1中且不在2中
print(list_2.difference(list_1))     #取差集，在2中且不在1中

#判断是否是list_1的子集
print(list_1.issubset(list_2))
print(list_1.issuperset(list_2))

#对称差集(在1或2中，但不会同时出现在二者中)------->并集-交集
print(list_1.symmetric_difference(list_2))
print("--------------------------------")

#增删改查
list_1.add(999)
print(list_1)

list_1.update([555,666,777])  #增加多项
