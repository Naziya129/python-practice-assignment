#QUIZ 1
# DEFAULT AND PARAMETRIZED CONSTRUCTORS
# A constructor is a special method that is automatically called when an object of a class is created.
# It is used to initialize the attributes of the class.

class Student:

    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print()

# Default constructor
s1 = Student()

# One-argument constructor
s2 = Student("Naziya")

# Two-argument constructor
s3 = Student("Aisha", 22)

s1.display()
s2.display()
s3.display()



#---------------------------------------------------
#QUIZ 2
# CALLING PARENT CONSTRUCTOR
# A child class can call the constructor of its parent class using the super() function.

class Parent:

    def __init__(self):
        print("Parent Constructor Called")

class Child(Parent):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def display(self):
        print("Child Name:", self.name)

c = Child("Naziya")
c.display()




#---------------------------------------------------
#QUIZ 3
# SIMULATING ACCESS LEVELS
# In Python, there are no strict access modifiers like private or protected.
# However, we can simulate access levels using naming conventions.

class Student:

    def __init__(self):
        self.name = "Naziya"          # Public
        self._course = "Python"       # Protected
        self.__salary = 25000         # Private

    def show_private(self):
        print("Private:", self.__salary)

obj = Student()

print("Public:", obj.name)

print("Protected:", obj._course)

obj.show_private()



#---------------------------------------------------
#QUIZ 4
# CONSTRUCTOR ATTRIBUTES
# Constructor attributes are the attributes that are initialized in the constructor of a class.

class Employee:

    def __init__(self):
        self.name = "Naziya"
        self.id = 101
        self.salary = 50000

emp = Employee()

print("Name:", emp.name)
print("ID:", emp.id)
print("Salary:", emp.salary)




#---------------------------------------------------
#QUIZ 5
# USING __STR__METHOD
# The __str__ method is used to define a string representation of an object.

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

s = Student("Naziya",22)

print(s)



#---------------------------------------------------
#QUIZ 6
# CONSTRUCTOR WITH *args
# A constructor can accept a variable number of arguments using *args.

class Numbers:

    def __init__(self, *args):
        self.values = args

    def display(self):
        print("Values:", self.values)

n = Numbers(10,20,30,40,50)

n.display()



#---------------------------------------------------
#QUIZ 7
# REAL-WORLD EXAMPLE(EMPLOYEE CLASS)
# A constructor initilizes object data when multiple objects are created from a class.

class Employee:

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)
        print()

emp1 = Employee("Naziya",101,50000)

emp2 = Employee("Aisha",102,45000)

emp3 = Employee("Rahul",103,55000)

emp1.display()

emp2.display()

emp3.display()