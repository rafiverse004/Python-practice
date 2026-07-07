# A constructor initializes an object when it is created.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


student = Student("Alice", 20)

student.display()