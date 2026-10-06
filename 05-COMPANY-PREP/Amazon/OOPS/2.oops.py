#student
class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
student1=student("anush",22,54)
student2=student("Sen",23,34)
student3=student("dhanish",24,45)

print(student1.name,student1.age)
print(student2.name)
#
class Student:
    def __init__(self,age,name,marks):
        self.age=age
        self.name=name
        self.marks=marks


    def display(self):
        print(self.name)
        print(self.age)
        print(self.marks)
    def check_grade(self):
        if self.marks>35:
            return f"A-grade"
        else:
            return f"B-grade"


student1=Student(23,'mahan',45)
student1.display()
print(student1.check_grade())
