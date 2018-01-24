# Author: Li tianyang

class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teacher = []

    def enroll(self,stu_obj):
        print("为学院%s 办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,staff):
        print("为学院招聘%s" % staff.name)
        self.teacher.append(staff)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        ---- info of Teacher: %s ----
         Name：%s
         Age：%s
         Sex：%s
         Salary：%s
         Course：%s
        ''' %(self.name,self.name,self.age,self.sex,self.salary,self.course))
    def teach(self):
        print("%s is teaching course [%s]"%(self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student, self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade


    def tell(self):
        print('''
        ---- info of Student: %s ----
         Name：%s
         Age：%s
         Sex：%s
         Stu_id：%s
         Grade：%s
        ''' %(self.name,self.name,self.age,self.sex,self.stu_id,self.grade))

    def pay_tuition(self,amount):
        print("%s has paid the tuition for $%s" % (self.name,amount))


school = School("Old Boy","东北大学")
t1 = Teacher("litianyang",23,"man",2000000,"Linux")
t2 = Teacher("Alex","32","man",8222,"python3")
s1 = Student("JsensonYang",23,"man",1700359,"Python")
s2 = Student("主要是气质好",23,"man",20133359,"Python")

t1.tell()
s1.tell()

school.enroll(s1)
school.hire(t1)

print(school.students)
print(school.teacher)

school.teacher[0].teach()
