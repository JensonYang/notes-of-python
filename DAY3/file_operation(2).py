# Author:Li tianyang
#在file_operation(1)中文件读取时，在内存中读一行删除一行，在内存中永远只有一行，所以无论文件多大都可以进行读取

'''High Loop'''
f = open('yesterday when I was young', 'r', encoding='utf-8')
'''count = 0

for line in f:              #这种效率是最高的
    if count == 10:
        print('--------------------------------------------------------------------------------------------------------我是分割线')
        count += 1
        continue
    print(line.strip())
    count += 1'''
print(f.flush())