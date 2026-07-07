# Special methods customize how objects behave.

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"


student = Student("Alice")

print(student)