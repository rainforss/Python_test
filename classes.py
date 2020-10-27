class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self, number):
        print(f"WOOF! My name is {self.name} and the number is {number}")


mydog = Dog(name="ape", breed="lab")

mydog.bark(3)


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

