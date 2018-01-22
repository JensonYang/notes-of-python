# Author:Li tianyang
f = open('yesterday when I was young', 'r', encoding='utf-8')
#tell 显示出在文件中光标在哪（按字符的个数）
print(f.tell())
print(f.readline()) #只打印一行
print(f.readline())
print(f.readline())
print(f.tell())
#现在想把光标移回去
print(f.seek(0))
print(f.readline())

#flush 刷新的意思：
print(f.flush())
