# QUIZ 1
#GENERATE AN EXCEPTION
# An exception is an error that occurs during the execution of a program.

#num = 10
#result = num / 0

#print(result)




#---------------------------------------------------
# QUIZ 2
# HANDLE THE EXCEPTION
# The try-except block is used to handle exceptions in python.

try:
    num = 10
    result = num / 0
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero.")



#---------------------------------------------------
# QUIZ 3
#  MULTIPLE EXCEPTIONS BLOCKS
# Multiple except blocks can be used to handle different types of exceptions.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Result:", num1 / num2)

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except ValueError:
    print("Please enter valid numbers.")




#---------------------------------------------------
# QUIZ 4
# RAISE AN EXCEPTION MANUALLY
# Raise is used to generate an exception manually in python.

def check_age(age):
    if age < 18:
        raise Exception("Age must be 18 or above.")

    print("Eligible")

age = int(input("Enter Age: "))

check_age(age)



#---------------------------------------------------
# QUIZ 5
# FUNCTIONS THAT RAISES AN EXCEPTION
# A function can raise an exception to indicate an error condition.


def error_function():
    raise Exception("This is a custom exception.")

# Without handling
# error_function()

# With handling
try:
    error_function()

except Exception as e:
    print(e)




#---------------------------------------------------
# QUIZ 6
# CREATE YOUR OWN EXCEPTION CLASS
# Custom exception classes can be created by inheriting from the built-in Exception class.

class InsufficientBalanceError(Exception):
    pass

balance = 500
withdraw = 700

try:
    if withdraw > balance:
        raise InsufficientBalanceError("Insufficient Balance")

    print("Transaction Successful")

except InsufficientBalanceError as e:
    print(e)





#---------------------------------------------------
# QUIZ 7
# USING FINALLY BLOCK
# The finally blocks is used to excute code regardless of whether an exception occurred or not.

try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    try:
        file.close()
        print("File Closed")
    except:
        pass





#---------------------------------------------------
# QUIZ 8
# FILE NOT FOUND EXCEPTION
# FileNOTFoundError occurs when trying to access a file that does not exist.

try:
    file = open("abc.txt", "r")

except FileNotFoundError:
    print("File does not exist.")





#---------------------------------------------------
# QUIZ 9
# TYPE ERROR EXCEPTION
# TypeError occurs when an operation is performed on an object of an inapproriate type.

try:
    result = "10" + 5

except TypeError:
    print("Cannot add string and integer.")





#---------------------------------------------------
# QUIZ 10
# ATTRIBUTE ERROR EXCEPTION
# AttributeError occurs when an invalid attribute is accessed on an object.

try:
    num = 100

    num.append(50)

except AttributeError:
    print("Attribute does not exist.")




#---------------------------------------------------
# QUIZ 11
# INDEX ERROR EXCEPTION
# IndexError occurs whwn trying to access an index that is out of range for a list or string.

numbers = [10,20,30]

try:
    print(numbers[5])

except IndexError:
    print("Invalid Index.")





#---------------------------------------------------
# QUIZ 12
# USE ELSE BLOCK WITH TRY-EXCEPT
# The else block can be used with try-except to execute code when no exception occurs.

try:
    num1 = 20
    num2 = 10

    print(num1 / num2)

except ZeroDivisionError:
    print("Division by zero.")

else:
    print("Program executed successfully.")





#---------------------------------------------------
# QUIZ 13
# LOGGING ERRORS 
# The logging module can be used to log errors and exceptions in python.

import logging

logging.basicConfig(filename="error.log", level=logging.ERROR)

try:
    result = 10 / 0

except Exception as e:
    logging.error(e)
    print("Error has been logged.")




#---------------------------------------------------
# QUIZ 14
# INPUT VALIDATION SYSTEM
# Input validation is the process of ensuring that user input meets certain criteria before being processed.

while True:

    try:
        age = int(input("Enter your age: "))

        print("Age:", age)

        break

    except ValueError:
        print("Please enter a valid number.")








