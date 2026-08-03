# Import is used to access classes and functions from another module.

import Packages.class_one
from Packages.class_two import ClassTwo

obj1 = Packages.class_one.ClassOne()
obj2 = ClassTwo()

obj1.display()
obj1.course()

obj2.display()
obj2.company()

# A complete program creates objects and calls methods from multiple classes.

import Packages.class_one
from Packages.class_two import ClassTwo

print("Program Started")

obj1 = Packages.class_one.ClassOne()
obj2 = ClassTwo()

obj1.display()
obj1.course()

obj2.display()
obj2.company()

print("\nCalling ClassOne from ClassTwo")

obj2.call_class_one()

print("\nProgram Finished")



# Alias import

# obj = c1.ClassOne()

# obj.display()

# obj.course() 