# Author: Li tianyang

# 嵌套函数: 在一个函数体内 要用def去声明一个函数 才叫嵌套函数

def foo():
    print("in the foo")
    def bar():
        print("in the bar")

    bar()
foo()

