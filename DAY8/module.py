# Author: Li tianyang

1.定义
模块：用来从逻辑上组织python代码（变量，函数，类，逻辑：实现一个功能），本质上就是.py结尾的python文件
包：用来从逻辑上组织模块的，本质上就是一个目录（必须带有一个_init_.py文件）
2.导入方法
import module_name
import module_name1,module_name2,...
# from module_name import *  >>>>>>>>>>>>>导入模块中所有东西 （不建议这么去使用  忘记它） 并不是导入模块，而是所有代码导入过来
# from module_name import m1,m2,m3
# from module_name import logger as logger1 >>>>>>为了防止冲突，用as重新起了一个名字
3.import的本质（路径搜索和搜索路径）
# import module_name
# module_name = all_code  导入了模块  相当于模块中所有的变量都赋值给了module_name    (先解释了一遍)
# from module_name import name 只解释了模块中的name，并赋值给了module_name,所以使用name并不用加上前缀
# 导入模块的本质就是把python文件解释一遍
# （1）import 得先有一个找的过程，找到之后才会解释执行一遍
# （2）sys.path
# 导入包的本质就是把_init_.py文件解释一遍

4.导入优化
# 为了避免重复调用 应该import module_name >>>>>>>>改成 from module_name import text(需要调用的那个变量或者函数名)
5.模块的分类
# （1）标准库
# （2）开源模块 第三方库
# （3）自定义模块