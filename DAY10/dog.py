# Author: Li tianyang



class Dog:
    def __init__(self,name):
        self.name = name
    def bulk(self):
        print("%s:Wang,wang,wang!" %  self.name)


d1 = Dog("A1")
d2 = Dog("A2")
d3 = Dog("A3")

d1.bulk()
d2.bulk()
d3.bulk()