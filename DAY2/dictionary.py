# Author:Li tianyang

#key-value 冒号前的是key
info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}
print(info)                  #字典是无序的，它没有下标。字典有 key！！
#print(info['stu1101'])      #直接查找字典中的信息
info['stu1101'] = '武藤兰'    #直接修改字典中的信息
info['stu1104'] = '苍老师'    #直接添加字典中的信息
del info['stu1101']          #直接删除字典中的信息
#info.pop('stu1101')          #也是直接删除
print(info.get('stu1101'))     #安全的获取 有>>>返回  无>>>None

print('stu1101' in info)     #查找stu1101是否在info中

#info.update()     #字典合并，相同项覆盖

for i in info:              #字典的循环
    print(i, info[i])
