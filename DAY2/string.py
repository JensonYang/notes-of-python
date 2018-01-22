# Author:Li tianyang

name = "My name is {name} and i am {year} old."

print(name.capitalize())        # 按“点”>>>>>.之后看到的功能 带两个下划线的都不是我们能用的（内部）
print(name.center(50,"-"))      #一共需要打印五十个字符，name在中间，如果不够用“-”补上
#print(name.endswith())          #判断以什么结尾
#print(name.expandtabs())        #没啥用
#print(name.find())              #查找A,找到返回其索引， 找不到返回-1

print(name.format(name="Litianyang", year="23"))
print(name.isdigit())            #判断是不是数字 是>>>返回为真  否>>>返回为假
print('+'.join(['1','2','3']))
print(name.ljust(50,'*'))        # 长度为50，不够50,在后面用*补上
print(name.rjust(50,'*'))        # 长度为50，不够50,在前面用*补上

p = str.maketrans("abcdef",'123456')    #类似于加密 （编码规则）
print("alex li".translate(p))
print('Li tian yang'.split(' '))     #按空格默认分成列表


