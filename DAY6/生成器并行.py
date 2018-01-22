# Author: Li tianyang


# 本质上还是单线程的
__author__ = 'Alex Li'

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))


def producer(name):
    c = consumer('A')           # 这里要明确 consumer已经不是一个函数了  而是一个生成器 此句赋值并不会让生成器往下走
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)                   #send 会给 yield 传值
        c2.send(i)

producer("alex")

