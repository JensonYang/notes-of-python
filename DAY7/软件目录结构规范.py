# Author: Li tianyang

# 项目目录组织结构如下：
# Foo/  　　　　　　　　# 项目名
#     --bin/   　　　　# 可执行文件目录
#         --foo　　　　# 可执行程序                              启动的脚本在这
#     --core/ 　　　　 # 主程序目录
#         --test/　　　# 测试用例（用于对项目中功能性测试）
#             --__init__.py
#             --test_main.py
#         --__init__.py
#         --main.py　　# 主程序入口                              但是程序的主入口是在这里的！
#     --conf/　　　　　# 配置文件目录
#         --settings.py  #配置文件
#     --logs/　　　　　# 日志文件目录
#         --log　　　　# 日志文件
#     --docs/ 　　　　 # 文档类目录
#     --setup.py   　 # 安装部署脚本
#     --requirements.txt  #依赖关系，存放依赖的软件包名称，
#     --README 　　　　# 程序说明
#
# 个别说明：
# README内容说明
# 1：软件定位，软件的基本功能
# 2：运行代码的方式：安装环境，启动命令等。
# 3：简要的使用说明。
# 4：代码目录结构说明，更详细可以说明软件的基本原理
# 5：常见问题说明。
#
# requirements.txt
# 文件格式是一行包含一个包依赖的说明，要求这个格式能被pip识别，使用方式：
# pip install -r requirements.txt   来安装所有依赖的包
#
# 以上各个目录模块如何动态导入，实现动态迁移。
# import os
# import sys
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
# 这里：通过动态导入项目的当前根路径即可