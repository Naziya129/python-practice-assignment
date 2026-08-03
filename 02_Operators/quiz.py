# QUIZ 1
# BASIC ARITHMETIIC OPERATION
#Arithmetic operators perform mathematical calculations such as addition, subtraction, multiplication, and division.

def arithmetic_operations(num1, num2):

    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)
    print("Division:", num1 / num2)

number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))

arithmetic_operations(number1, number2)



#-------------------------------------------------------
#QUIZ 2
# SIMULAING INCREMENT AND DECREMENT
#Python uses += 1 for increment and -= 1 for decrement because it does not support ++ or --.

def increment_decrement(number):

    print("Original Value:", number)

    number += 1
    print("After Increment:", number)

    number -= 1
    print("After Decrement:", number)

num = int(input("Enter a Number: "))

increment_decrement(num)




#-------------------------------------------------------
#QUIZ 3
# CHECK IF TWO NUMBERS ARE EQUAL
#The == operator checks whether two values are equal.

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if num1 == num2:
    print("Both numbers are Equal")

else:
    print("Both numbers are Not Equal")





#-------------------------------------------------------
#QUIZ 4
# RELATIONAL OPERATORS DEMONSTRATION
#Relational operators compare two values and return either True or False.

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Less Than (<):", num1 < num2)
print("Less Than or Equal (<=):", num1 <= num2)
print("Greater Than (>):", num1 > num2)
print("Greater Than or Equal (>=):", num1 >= num2)





#-------------------------------------------------------
#QUIZ 5
# FIND SMALLER AND LARGER NUMBERS
# Comparison operators help determine the smaller and larger values between two numbers

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if num1 > num2:
    print("Smaller Number:", num2)
    print("Larger Number:", num1)

else:
    print("Smaller Number:", num1)
    print("Larger Number:", num2)





#-------------------------------------------------------
#QUIZ 6
# COMBINE CONDITIONS
# Logical and comparison operators can be combined to compare multiple values.

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest Number:", num1)

elif num2 >= num1 and num2 >= num3:
    print("Largest Number:", num2)

else:
    print("Largest Number:", num3)





#-------------------------------------------------------
#QUIZ 7
# OPERATOR-BASED CALCULATOR
# A calculator uses arithmetic operators and conditional statements to perform calculations based on the user's choice.

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

operator = input("Enter Operator (+, -, *, /): ")

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":

    if num2 != 0:
        print("Result:", num1 / num2)

    else:
        print("Division by zero is not allowed.")

else:
    print("Invalid Operator")