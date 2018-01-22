# Author: Li tianyang

# 递归
def calc(n):
    print(n)
    if int(n/2) == 0:
        return n    #函数真正是在这里结束的，
    return calc(int(n/2))       # 自己调用自己，在这里实现的递归

calc(10)

#递归实例，二分查找

