# Author: Li tianyang


# 两点声明：
#            （1）Python中是贪婪模式：尽可能“贪婪”地多给我们匹配字符
#            （2）转义字符\        : 在正则表达式里，这个符号通常用来把特殊的符号转成普通的

import re

# 为了限制python中的贪婪模式，只要在“+”后面加一个“？”,
# 加了一个“?”我们就将贪婪的“+”改成了懒惰的“+”。这对于[abc]+,\w*之类的同样适用。
key = r"chuxiuhong@hit.edu.cn"
p1 = r"@.+?\."                                  #我想匹配到@后面一直到“.”之间的，在这里是hit
pattern1 = re.compile(p1)
print (pattern1.findall(key))


##  个人建议：在你使用"+","*"的时候，
## 一定先想好到底是用贪婪型还是懒惰型，
## 尤其是当你用到范围较大的项目上时，
## 因为很有可能它就多匹配字符回来给你


# 为了能够准确的控制重复次数，正则表达式还提供
# {a,b}(代表a<=匹配次数<=b)
key = r"saas and sas and saaas"
p1 = r"sa{1,3}s"
pattern1 = re.compile(p1)
print(pattern1.findall(key))