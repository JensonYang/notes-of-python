# Author: Li tianyang

def test(x,y):
    print(x)
    print(y)

test(y=1,x=2)    #关键字调用，与形参位置无关
test(1, 2)       #位置调用与形参位置一一对应
test(3,y=2)      #这种可以运行，按照顺序就可以运行
#test(x=2,3)     #不能执行
'''总结起来就一句话：
                关键字调用一定要在位置调用后面
'''