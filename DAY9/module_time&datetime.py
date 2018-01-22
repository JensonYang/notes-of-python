# Author: Li tianyang

# 标准库：
# time and datatime
# 记住笔记上的转化关系 即可////////或者使用help指令

import time
a = time.time()                  #距离1970年的秒数
print(1970+a/3600/24/365)        #1970年第一个操作系统诞生

print(time.localtime())         # 当地时间   isdst = 时区  英国格林尼治天文台：中间的叫本初子午线，北京在东八区，新疆在懂五区，比标准时间早八个小时

# gmtime() -- convert seconds since Epoch to UTC tuplegmtime() -- convert seconds since Epoch to UTC tuple
# help(time)

print(time.strftime("%Y/%m/%d %H:%M:%S"))