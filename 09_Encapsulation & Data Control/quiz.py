# QUIZ 1
# CREATE A SIMPLE
# A class groups data (attributes) and functions (methods) into a single unit.

class Student:

    def set_values(self, name, age):
        self.name = name
        self.age = age

    def get_values(self):
        print("Name:", self.name)
        print("Age:", self.age)

student = Student()

student.set_values("Naziya", 22)

student.get_values()


#-------------------------------------------------------
# QUIZ 2
# VALIDATON USING METHODS
# Validation checks whether data satisfies required conditions before storing it.

class Student:

    def set_values(self, name, age):

        self.name = name

        if age > 0:
            self.age = age
        else:
            print("Invalid Age")
            self.age = 0

    def get_values(self):
        print("Name:", self.name)
        print("Age:", self.age)

student = Student()

student.set_values("Naziya", -5)

student.get_values()




#-------------------------------------------------------
# QUIZ 3
# PROPERTY DECORATOR
# @property and @setter provide controlled access to object attributes.

class Student:

    def __init__(self):
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value > 0:
            self._age = value
        else:
            print("Invalid Age")

student = Student()

student.age = 22

print(student.age)




#-------------------------------------------------------
# QUIZ 4
# READ-ONLY PROPERTY
# A read-only property can be accessed but cannot be modified after object creation.

class Employee:

    def __init__(self, emp_id):
        self._id = emp_id

    @property
    def id(self):
        return self._id

employee = Employee(101)

print(employee.id)





#-------------------------------------------------------
# QUIZ 5
# BANK ACCOUNT SYSTEM
# Encapsulation protects data by allowing access only through methods.

class BankAccount:

    def __init__(self, account_holder, balance):

        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

        print("Balance:", self.balance)

    def withdraw(self, amount):

        if amount <= self.balance:

            self.balance -= amount

            print("Balance:", self.balance)

        else:
            print("Insufficient Balance")

account = BankAccount("Naziya",5000)

account.deposit(1000)

account.withdraw(2000)

account.withdraw(5000)





#-------------------------------------------------------
# QUIZ 6
# INTERNAL VARIABLES
# Variables starting with _ are intended for internal use by convention.

class Demo:

    def __init__(self):

        self._message = "Internal Variable"

demo = Demo()

print(demo._message)





#-------------------------------------------------------
# QUIZ 7
# COMPUTED PROPERTY 
# A computed property calculates its value automatically when accessed.

class Rectangle:

    def __init__(self, length, width):

        self.length = length
        self.width = width

    @property
    def area(self):

        return self.length * self.width

rectangle = Rectangle(10,5)

print("Area:", rectangle.area)





#-------------------------------------------------------
# QUIZ 8
# PASSWORD VALIDATION SYSTEM
# Password validation checks whether a password satisfies required security rules.

class User:

    def __init__(self):
        self._password = ""

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):

        if len(value) < 8:
            print("Password must be at least 8 characters.")

        elif not any(char.isdigit() for char in value):
            print("Password must contain at least one number.")

        else:
            self._password = value
            print("Password Accepted")

user = User()

user.password = "Python123"

print(user.password)





