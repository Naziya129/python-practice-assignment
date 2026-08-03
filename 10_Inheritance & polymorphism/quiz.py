# QUIZ 1
# CREATE CLASS HIERARCHY
# Multilevel inheritance allows one class to inherit from another, forming a chain of inheritance.

class A:
    pass

class B(A):
    pass

class C(B):
    pass

print("Class Hierarchy Created Successfully")



#----------------------------------------------------
# QUIZ 2
# DEFINE METHODS
# Method overriding allows a child class to provide its own implementation of a parent class method.

class A:

    def method1(self):
        print("Method 1 of Class A")

    def method2(self):
        print("Method 2 of Class A")

    def common(self):
        print("Common Method from Class A")


class B(A):

    def method3(self):
        print("Method 1 of Class B")

    def method4(self):
        print("Method 2 of Class B")

    def common(self):
        print("Common Method from Class B")


class C(B):

    def method5(self):
        print("Method 1 of Class C")

    def method6(self):
        print("Method 2 of Class C")

    def common(self):
        print("Common Method from Class C")




#----------------------------------------------------
# QUIZ 3
# OBJECT CREATION AND METHOD CALLS
# Objects are used to access methods and attributes of a class.

a = A()

b = B()

c = C()

a.method1()
a.method2()
a.common()

print()

b.method1()
b.method2()
b.method3()
b.method4()
b.common()

print()

c.method1()
c.method2()
c.method3()
c.method4()
c.method5()
c.method6()
c.common()





#----------------------------------------------------
# QUIZ 4
# SUPERCLASS REFERENCE BEHAVIOUR (RUNTIME POLYMORPHISM)
# Runtime polymorphism executes the overridden method of the actual object at runtime.

reference = B()

reference.common()

reference = C()

reference.common()





#----------------------------------------------------
# QUIZ 5
# ACCESS PARENT METHOD USING super()
# super() calls the parent class method from the child class.

class A:

    def common(self):
        print("Class A Method")


class B(A):

    def common(self):
        super().common()
        print("Class B Method")


class C(B):

    def common(self):
        super().common()
        print("Class C Method")


obj = C()

obj.common()




#----------------------------------------------------
# QUIZ 6
# INSTANCE VARIABLES BEHAVIOR
# Instance variables with the same name in different classes hide the parent variable.

class A:

    def __init__(self):
        self.name = "Class A"


class B(A):

    def __init__(self):
        super().__init__()
        self.name = "Class B"


class C(B):

    def __init__(self):
        super().__init__()
        self.name = "Class C"


a = A()

b = B()

c = C()

print(a.name)

print(b.name)

print(c.name)

reference = C()

print(reference.name)





#----------------------------------------------------
# QUIZ 7
# CONSTRUCTOR EXECUTION ORDER
# Constructors execute from the parent class to the child class when using super().

class A:

    def __init__(self):
        print("Constructor of Class A")


class B(A):

    def __init__(self):
        super().__init__()
        print("Constructor of Class B")


class C(B):

    def __init__(self):
        super().__init__()
        print("Constructor of Class C")


obj = C()




#----------------------------------------------------
# QUIZ 8
# REAL-WORLD EXAMPLE
# Inheritance models real-world relationships by allowing specialized classes to extend general classes.

class Vehicle:

    def start_engine(self):
        print("Vehicle Engine Started")


class Car(Vehicle):

    def start_engine(self):
        print("Car Engine Started")


class ElectricCar(Car):

    def start_engine(self):
        print("Electric Car Started Silently")


vehicle = Vehicle()

car = Car()

electric = ElectricCar()

vehicle.start_engine()

car.start_engine()

electric.start_engine()