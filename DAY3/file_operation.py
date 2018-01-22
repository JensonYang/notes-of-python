# Author:Li tianyang

#要对打开的文件附一个变量 ，才能进行后续的操作
f = open("yesterday when I was young", 'a',encoding="utf-8",) #文件句柄 'r'就是读模式
#f = open("yesterday when I was young", 'w',encoding="utf-8",) #文件句柄 'w'是写模式，创建模式，空文件

f.write("\n when I was young I listen to the radio.")
data = f.read()
print(data)

"""打开文件的模式有：
•r，只读模式（默认）。
•w，只写模式。【不可读；不存在则创建；存在则覆盖内容；】
•a，追加模式。【不可读；不存在则创建；存在则只追加内容；】
'''

