# Author:Li tianyang
#names = "Zhangyang, Guyun, Xiangpeng, Litianyang" 每个名字不能单独取出来

names = ["Zhangyang", "Guyun", "Xiangpeng", "Litianyang"]

print(names[1:3])                #切片      >>>>>>>>>>>>>>>同时取多个元素时法则： 顾头不顾尾
print(names[:3])                 #切片      >>>>>>>>>>>>>>>同时取多个元素时法则： 顾头不顾尾
print(names[-1])                 #切片      >>>>>>>>>>>>>>>同时取多个元素时法则： 顾头不顾尾
print(names[-3:-1])              #切片      >>>>>>>>>>>>>>>同时取多个元素时法则： 顾头不顾尾

names.append("我是新来的!")      #追加 >>>>>>>>> 不指定位置即放在最后  append

names.insert(1, "我是新来的!")   #插入 >>>>>>>>> 指定位置，插在谁之后  insert

names[2] = "Tianyang"           #修改 >>>>>>>>> 直接赋值修改

names.remove("Tianyang")        #删除
del names[1]                    #删除
names.pop()                     #删除    不输入下标，or default last one

print(names.index("Litianyang"))#获取已知元素名称的下标
print(names[names.index("Litianyang")])    #多此一举，但是一会练习的时候就有用了

names.count("")                 #统计   统计有几个相同元素
#names.clear()                  #清空
names.reverse()                 #反转   完全颠倒顺序
names.sort()                    #排序，默认先字符，后数字，最后按字母顺序  ABCD....
names.extend([1, 2, 3])
print(names)
names.remove()
print(names)

