# Instance variables belong to each object, while class variables are shared.

class Student:
    school = "Eastern University"

    def __init__(self, name):
        self.name = name


student1 = Student("Alice")
student2 = Student("Bob")

print(student1.name)
print(student2.name)

print(student1.school)
print(student2.school)

Student.school = "OpenAI Academy"

print(student1.school)
print(student2.school)