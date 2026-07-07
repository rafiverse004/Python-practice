# Classes can have instance, class, and static methods.

class Student:
    school = "Eastern University"

    def __init__(self, name):
        self.name = name

    # Instance method
    def introduce(self):
        print(f"My name is {self.name}.")

    # Class method
    @classmethod
    def show_school(cls):
        print(f"School: {cls.school}")

    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18


student = Student("Alice")

student.introduce()

Student.show_school()

print(Student.is_adult(20))