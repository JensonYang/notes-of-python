# Author:Li tianyang

#import sys

#print(sys.path)        #打印环境变量  模块通过“.”点来展现其功能

import passwd          # .pyc 就是再一次运行时 快速加载。



''' 
    其运行结果的意思为，sys的模块必须在这些路径下当中至少有一个路径有sys模块，不然报错。
'''
''''
    F:\\Python\\lib\\site-packages',——————————————>Python自带的标准库一般都存在这个目录下
'''
'''
print(sys.argv)       #脚本名字的绝对路径
print(sys.argv[2])   
'''

'''import os
cmd_res = os.system("dir")
print("--->",cmd_res)         #结果为0 说明执行成功'''



msg = "我爱北京天安门"
print(msg)
print(msg.encode("utf-8"))