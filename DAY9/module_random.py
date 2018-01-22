# Author: Li tianyang

import random

print(random.random())          # 生成0-1随机数

print(random.randint(5,9))      #生成5-9之间整数，包括5,9

print(random.randrange(5,8))    # 生成5 6 7 不包括8

# 生成随机验证码
checkcode = ''

for i in range(4):

    current = random.randrange(0,4)

    if current != i:

        temp = chr(random.randint(65,90))   #  ASCII码的对应关系

    else:

        temp = random.randint(0,9)    #此处不能加10，不然会多一位   四位变五位

    checkcode += str(temp)

print(checkcode)
# -------------------------------------------------------------------------------

print(chr(1200))