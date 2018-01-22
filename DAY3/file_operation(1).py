# Author:Li tianyang

f = open("yesterday when I was young", 'r',encoding='utf-8')
#f.readlines 变成列表   其中一行为一个元素
#f.readlines只适合读小文件，若文件为2G大小，从硬盘读到内存上时是读全部内容，太慢！！！
for index,line in enumerate(f.readlines()):  #获取下标
    if index == 9:
        print('---------------------------我是分隔符')
        continue

    print(line.strip())                 #strip：把空格和换行都去掉
#for i in range(10):
#    print(f.readline())