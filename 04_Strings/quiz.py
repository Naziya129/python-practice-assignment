# QUIZ 1
# CREATING STRINGS IN DIFF WAYS
# Strings can be created using single quotes, double quotes, or triple quotes.

string1 = 'Hello'

string2 = "Python"

string3 = '''Welcome to
JALA Academy'''

print(string1)
print(string2)
print(string3)


#---------------------------------------------------
# QUIZ 2
# STRING CONCATENATION
# String concatenation combines two or more strings using the + operator.

first = "Hello"

second = "World"

result = first + " " + second

print(result)




#---------------------------------------------------
# QUIZ 3
# LENTH OF A STRING
# The len() function returns the total number of characters in a string.

text = "Python"

print("Length:", len(text))






#---------------------------------------------------
# QUIZ 4
# EXTRACT SUBSTRING
# Slicing extracts a part of a string using index positions.

text = "Python Programming"

print(text[0:6])




#---------------------------------------------------
# QUIZ 5
# SEARCH IN STRING
# find() returns -1 if not found, while index() raises an error if not found.

text = "Python Programming"

print("Find:", text.find("Program"))

try:
    print("Index:", text.index("Java"))

except ValueError:
    print("Substring not found.")





#---------------------------------------------------
# QUIZ 6
# COMPARE STRINGS
# Strings can be compared using equality (==) and inequality (!=) operators.

str1 = "Python"

str2 = "Python"

print(str1 == str2)

print(str1 != str2)






#---------------------------------------------------
# QUIZ 7
# STARTSWITH() AND ENDSWITH()
# startswith() and endswith() check the beginning and ending of a string.

text = "Python Programming"

print(text.startswith("Python"))

print(text.endswith("Programming"))





#---------------------------------------------------
# QUIZ 8
# LEXICOGRAPHICAL COMPARISON
# Lexicographical comparison compares strings based on dictionary order.

str1 = "Apple"

str2 = "Banana"

if str1 > str2:
    print(str1, "is greater")

elif str1 < str2:
    print(str2, "is greater")

else:
    print("Both are equal")





#---------------------------------------------------
# QUIZ 9
# TRIM WHITESPACES
# strip() removes leading and trailing spaces from a string.

text = "   Python Programming   "

print(text.strip())





#---------------------------------------------------
# QUIZ 10
# REPLACE CHARACTERS
# replace() replaces a character or word with another value.

text = "I like Java"

print(text.replace("Java", "Python"))




#---------------------------------------------------
# QUIZ 11
# SPLIT A STRING
# split() divides a string into a list based on a separator.

text = "Python Java SQL"

print(text.split())



#---------------------------------------------------
# QUIZ 12
# CONVERT INTEGER TO STRING
# str() converts an integer into a string.

number = 100

text = str(number)

print(number, type(number))

print(text, type(text))





#---------------------------------------------------
# QUIZ 13
# UPPERCASEAND LOWERCASE
# upper() converts to uppercase and lower() converts to lowercase.

text = "Python"

print(text.upper())

print(text.lower())




#---------------------------------------------------
# QUIZ 14
# PATTERN MATCHING USING re MODULE
# The re module checks whether a string matches a specified pattern.

import re

email = "naziya123@gmail.com"

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(pattern, email):
    print("Valid Email")

else:
    print("Invalid Email")




#---------------------------------------------------
# QUIZ 15
# COUNT VOWELS AND CONSONANTS
# Vowels and consonants are counted by checking each alphabet character.

text = "Python"

vowels = 0

consonants = 0

for letter in text.lower():

    if letter.isalpha():

        if letter in "aeiou":
            vowels += 1

        else:
            consonants += 1

print("Vowels:", vowels)

print("Consonants:", consonants)





#---------------------------------------------------
# QUIZ 16
# REVERSE A STRING
# Slicing with [::-1] reverses a string.

text = "Python"

print(text[::-1])










 




