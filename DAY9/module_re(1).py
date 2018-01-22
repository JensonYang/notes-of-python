# Author: Li tianyang

'''自学部分'''

import re

# . : 字符在正则表达式代表着可以代表任何一个字符（包括它本身），
# + : 将前面一个字符或一个子表达式重复一遍或者多遍
key = r"<h1>hello world<h1>"            #源文本
p1 = r"<h1>.+<h1>"                      #我们写的正则表达式，下面会将为什么
pattern1 = re.compile(p1)
print(pattern1.findall(key))           #发没发现，我怎么写成findall了？咋变了呢？


# *：跟在其他符号后面表达可以匹配到它0次或多次
# ******与+++++是一组
key = r"http://www.nsfbuhwe.com and https://www.auhfisna.com"           #胡编乱造的网址，别在意
p1 = r"https*://"      #看那个星号！ 意思就是：s可以匹配也可以匹配很多次
pattern1 = re.compile(p1)
print(pattern1.findall(key))


#  []：字符集，匹配里面的字符中的任意一个，字符可以逐个列出也可以给出范围，如a-z
#  第一个字符如果是^，代表取反，如[^a-c]表示不是abc的其他字符
key = r"lalala<hTml>hello</Html>heiheihei"
p1 = r"<[Hh][Tt][Mm][Ll]>.+?</[Hh][Tt][Mm][Ll]>"                    # ?: 匹配前一个字符0次或1次
pattern1 = re.compile(p1)
print(pattern1.findall(key))

key = r"mat cat hat pat"
p1 = r"[^p]at"                  #这代表除了p以外都匹配
pattern1 = re.compile(p1)
print(pattern1.findall(key))
'''
[0-9]	0123456789任意之一
[a-z]	小写字母任意之一
[A-Z]	大写字母任意之一
\d	    等同于[0-9]
\D	    等同于[^0-9]匹配非数字
\w	    等同于[a-z0-9A-Z_]匹配大小写字母、数字和下划线
\W	    等同于[^a-z0-9A-Z_]等同于上一条取非
'''


