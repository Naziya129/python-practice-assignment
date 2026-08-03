# Each class can have its own constructor and methods.

from .class_one import ClassOne


class ClassTwo:

    def __init__(self):
        self.city = "Hyderabad"
        print("ClassTwo Constructor Called")

    def display(self):
        print("City:", self.city)

    def company(self):
        print("IT COMPANY")

    def call_class_one(self):
        obj = ClassOne()
        obj.display()