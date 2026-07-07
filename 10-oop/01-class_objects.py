# Classes are blueprints for creating objects.

class Student:
    def introduce(self):
        print("Hello, I am a student.")


# Create objects
student1 = Student()
student2 = Student()

student1.introduce()
student2.introduce()

print(student1)
print(student2)