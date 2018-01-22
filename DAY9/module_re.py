# Author: Li tianyang

# 正则表达式非常重要，爬虫里面需要用
# re 只要有返回就是匹配到了，没有返回就是没有匹配到

# re.match 从头开始匹配
#
# re.search 匹配包含
#
# re.findall 把所有匹配到的字符放到以列表中的元素返回
#
# re.splitall 以匹配到的字符当做列表分隔符
#
# re.sub      匹配字符并替换

import re

res = re.match(".+","Chen321Ronghua123")      #  .+ 匹配任意字符  若只有. 则只匹配到C
#print(res)
res1 = re.match("^","Chen321Ronghua123")      #  匹配字符开头:   match中^没有任何作用，因为本身就是从头开始
#print(res1)

# 现在的任务是 识别出Ronghua
#res2 = re.match("^R.+a$","Chen321Ronghua123")  不可行   有. 那么$永远不可能起作用
res3 = re.search("R.+a","Chen321Ronghua123")    #?????????   是不是这种表达式更符合逻辑呢？
print(res3)

res4 = re.search("R.+a","Chen321Ronghua123a")   # 从开头一直匹配到最后一个a
print(res4)

res5 = re.search("#.+#","11234#hello#")
print(res5)

# "?" 匹配前一个字符一次或者0次  >>>>>>前一个字符，若aaa，意思就是前面两个a必须要存在，第三个a可以匹配一次或者0次
res6 = re.search("aaaa?","abanyangaaa")
print(res6)

#匹配数字(有问题)
res7 = re.search("[0-9](2)+", "aa15151515158l51")
print(res7)

#findall   ??????
res8 = re.findall("[0-9]{2}", "aa15151515158l51")
print(res8)

#| 管道符，“或”的意思  但是findall 都能找到的
res9 = re.findall("abc|ABC", "aa15ABCdksabcjdk")
print(res9)

