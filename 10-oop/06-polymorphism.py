# Polymorphism allows the same method name to behave differently.

class Cat:
    def speak(self):
        print("Meow")


class Dog:
    def speak(self):
        print("Bark")


animals = [Cat(), Dog()]

for animal in animals:
    animal.speak()