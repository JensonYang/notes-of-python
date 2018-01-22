# Author: Li tianyang

# 项目主要的逻辑并不在这里，atm主要去调用main文件中的程序
# 这里不能写死了，不然移植性差>>>>>>>>>>>>>相对路径

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# __file__获取的是相对路径


sys.path.append(BASE_DIR)

from core import shopping_cart  # 动态添加的，所以会有红线

if __name__ == "__main__":
    shopping_cart.run()
