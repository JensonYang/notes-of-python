# Author:Li tianyang
#raw_input python2.x   input python3.x

name = input("name: ")
age = int(input("age: "))                          # 强制类型转换成int; age = ("intput: ")默认为str 字符串类型
print(type (age))                                  #------> 查询数据类型
job = input("job: ")
salary = input("salary: ")
info = '''
-----  info of %s--------
Name:%s
Age:%d 
Job:%s
Salary:%s
''' %(name,name,age,job,salary)         # 这种格式要记住，%s是占位符，有几个占位符就要写几个名
print(info)
#------------------------------------------------------------------------------------------------------------------

info2 = '''
-----  info of {_name}--------
Name: {_name}
Age: {_age}1
Job: {_job}
Salary: {_salary}
''' .format(_name=name,
            _age=age,
            _job=job,
            _salary=salary)
print(info2)
#------------------------------------------------------------------------------------------------------------
info3 = '''
-----  info of {0}--------
Name: {0}
Age: {1}
Job: {2}                                        # 感觉不清晰，不好。
Salary: {3}
''' .format(name,age,job,salary)
print(info3)