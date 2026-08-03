
#QUIZ 1
# Print your name
# print() is used to display output on the screen.


print("Aaru")
print("Hello India")



#---------------------------------------------------
# QUIZ 2
# comments in python
# Comments are used to explain the code and 
# ignored by Python during execution.


# A Single line comment

print("Women are strong, talented, and inspiring.")

# Multi-line comments can be created using triple quotes ('''or """)

print("Women's Day Celebration")

'''
Women play an important role in society.
They contribute to education, healthcare,
business, science, sports, and many other fields.
This is a multi-line comment using triple quotes.
'''

print("Comments help explain the purpose of the code and make it easier to understand.")





#---------------------------------------------------
# QUIZ 3
# Basics Data Types in python
# A data type specifies what kind of value a variable can store


integer_value = 10
float_value = 10.5
boolean_value = True
string_value = 'A'

print(integer_value, type(integer_value))
print(float_value, type(float_value))
print(boolean_value, type(boolean_value))
print(string_value, type(string_value))




#---------------------------------------------------
# QUIZ 4
#Local vs Global Variables in Python
# Global variables can be accessed anywhere, while 
# local variables exist only inside a function.


name = "Global Variable"

def display():
    name = "Local Variable"

    print("Local:", name)
    print("Global:", globals()['name'])

display()





#---------------------------------------------------
# QUIZ 5
# Type checking & Dynamic Typing in Python
# Python is dynamically typed, meaning the same variable can store different data types.


value = 10
print(value, type(value))

value = 10.5
print(value, type(value))

value = True
print(value, type(value))

value = "Python"
print(value, type(value))




#---------------------------------------------------
# QUIZ 6
# User Input practice
# input() is used to take input from the user during program execution.


name = input("Enter your name: ")
age = input("Enter your age: ")

print("Name:", name)
print("Age:", age)



