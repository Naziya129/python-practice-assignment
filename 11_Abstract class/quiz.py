# quiz 1
# ABSTRACT AND NON-ASBTRACT METHODS
# An abstract class contains at least one abstract method and cannot be instantiated directly.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def display(self):
        print("This is a non-abstract method.")

### no object created



#----------------------------------------------------------
# quiz 2 
# CREATE A CHILD CLASS
# A child class must implement all abstract methods of its parent abstract class.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def display(self):
        print("This is a non-abstract method.")

class Dog(Animal):

    def sound(self):
        print("Dog says: Bark")


### NO O/P (JUST A CLASS DEFINATIONS)




#----------------------------------------------------------
# quiz 3
# ACCESS NON-ABSTRACT METHOD VIA CHILD OBJECT
# A child object can access inherited non-abstract methods from its parent class.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def display(self):
        print("This is a non-abstract method.")

class Dog(Animal):

    def sound(self):
        print("Dog says: Bark")

dog = Dog()

dog.display()




#----------------------------------------------------------
# quiz 4 
# CALL ABSTRACT METHOD IMPLEMENTATION
# The abstract method is implemented in the child class and called through its object.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog says: Bark")

dog = Dog()

dog.sound()





#----------------------------------------------------------
# quiz 5 
# ATTEMPT TO INSTANTIATE ABSTRACT CLASS
# An abstract class cannot be instantiated because it contains unimplemented abstract methods.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

obj = Animal()

### TYPEERROR:





#----------------------------------------------------------
# quiz 6 
# MULTIPLE ABSTRACT METHODS
# A child class must implement every abstract method defined in the abstract class.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def food(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog says: Bark")

    def food(self):
        print("Dog likes Meat")

dog = Dog()

dog.sound()

dog.food()





#----------------------------------------------------------
# quiz 7 
# REAL-WORLD EXAMPLE
# Abstract classes define common behavior while subclasses provide specific implementations.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def display(self):
        print("Area Calculation")

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Circle Area:", 3.14 * self.radius * self.radius)

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Rectangle Area:", self.length * self.width)

c = Circle(5)

c.display()

c.area()

r = Rectangle(10,5)

r.display()

r.area()





#----------------------------------------------------------
# quiz 8 
# PARTIAL IMPLEMENTATION
# A subclass that does not implement all abstract methods also becomes abstract.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def food(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog says: Bark")

dog = Dog()






