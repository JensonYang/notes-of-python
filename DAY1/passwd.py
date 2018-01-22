# Author:Li tianyang
import getpass                 #这是python标准库中自带的模块，可以直接调用
                                #import 在pycharm中不好使!
_username = 'Li tianyang'
_password = 'abc123'
username = input("username:")
#password = getpass.getpass("password:")
password = input("pasword:")
if _username == username and _password == password:                #------>这个位置的冒号
    print("Welcome to login...")   #这个位置必须要强制缩进，省掉了结束符，结构更清晰
else:
    print("Invalid username or password!")

print("dddd")      #IndentationError: unindent does not match any outer indentation level
                   #缩进错误，python中必须要顶格写

#print(username,password)

