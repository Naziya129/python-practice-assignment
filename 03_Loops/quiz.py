# QUIZ 1
# PRINT A MESSAGE MULTIPLE TIMES
# A for loop repeats a block of code for a specified number of times.

for i in range(10):
    print("Bright IT Career")



#----------------------------------------------------
# QUIZ 2
# PRINT NUMBERS USING WHILE LOOP
# A while loop executes repeatedly as long as the given condition is true.

num = 1

while num <= 20:
    print(num)
    num += 1





#----------------------------------------------------
# QUIZ 3
# EQUAL AND NOT EQUAL CHECK
# The == operator checks equality, while != checks inequality.

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if num1 == num2:
    print("Both numbers are Equal")

if num1 != num2:
    print("Both numbers are Not Equal")



#----------------------------------------------------
# QUIZ 4
# ODD AND EVEN NUMBERS
# Even numbers are divisible by 2, while odd numbers are not divisible by 2.

print("Even Numbers:")

for i in range(1, 51):

    if i % 2 == 0:
        print(i)

print()

print("Odd Numbers:")

for i in range(1, 51):

    if i % 2 != 0:
        print(i)




#----------------------------------------------------
# QUIZ 5
# LARGEST AMONG THREE NUMBERS
# Conditional statements (if, elif, else) are used to compare values and make decisions.

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest Number:", num1)

elif num2 >= num1 and num2 >= num3:
    print("Largest Number:", num2)

else:
    print("Largest Number:", num3)




#----------------------------------------------------
# QUIZ 6
# EVEN NUMBERS IN A RANGE
# A while loop repeatedly executes a block of code until the condition becomes false.

num = 10

while num <= 20:

    if num % 2 == 0:
        print(num)

    num += 1




#----------------------------------------------------
# QUIZ 7
# ARMSTRONG NUMBER
# An Armstrong number is a number equal to the sum of its digits raised to the power of the number of digits.

number = int(input("Enter a Number: "))

original = number
digits = len(str(number))
total = 0

while number > 0:

    digit = number % 10
    total = total + digit ** digits
    number = number // 10

if total == original:
    print(original, "is an Armstrong Number")

else:
    print(original, "is Not an Armstrong Number")



#----------------------------------------------------
# QUIZ 8
# PRIME NUMBERS CHECK
# A prime number has exactly two factors: 1 and itself.

number = int(input("Enter a Number: "))

count = 0

for i in range(1, number + 1):

    if number % i == 0:
        count += 1

if count == 2:
    print(number, "is a Prime Number")

else:
    print(number, "is Not a Prime Number")




#----------------------------------------------------
# QUIZ 9
# PALINDROME CHECK
# A palindrome number reads the same forward and backward.

number = int(input("Enter a Number: "))

original = number
reverse = 0

while number > 0:

    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print(original, "is a Palindrome")

else:
    print(original, "is Not a Palindrome")





#----------------------------------------------------
# QUIZ 10
# EVEN OR ODD (USING CONDITION)
# The modulus operator (%) checks whether a number is even or odd.

number = int(input("Enter a Number: "))

if number % 2 == 0:
    print(number, "is Even")

else:
    print(number, "is Odd")



#----------------------------------------------------
# QUIZ 11
# GRNDER IDENTIFICATION
# Conditional statements (if, elif, else) are used to make decisions based on user input.

gender = input("Enter Gender (M/F): ")

if gender == "M" or gender == "m":
    print("Male")

elif gender == "F" or gender == "f":
    print("Female")

else:
    print("Invalid Input")



#----------------------------------------------------
# QUIZ 12
# MULTIPLICATION TABLE GENERATOR
# A loop can be used to generate the multiplication table of a number.

number = int(input("Enter a Number: "))

for i in range(1, 11):

    print(number, "x", i, "=", number * i)




#----------------------------------------------------
# QUIZ 13
# COUNT DIGITS IN A NUMBER
# The number of digits is counted by repeatedly dividing the number by 10 until it becomes 0.

number = int(input("Enter a Number: "))

count = 0

while number > 0:

    number = number // 10
    count += 1

print("Number of Digits:", count)



