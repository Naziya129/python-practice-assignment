# QUIZ 1
# FUNCTIONS WITH PARAMETERS
# A functions can accept parameters to perform operations on them.

def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)





#---------------------------------------------------
#QUIZ 2
# DEFAULT PARAMETERS
# A functions can have default parameters that are used if no argument is provided.

def greet(name, message="Hello"):
    print(message, name)

greet("Naziya")
greet("Aisha", "Welcome")




#---------------------------------------------------
#QUIZ 3
# KEYWORD ARGUMENTS
# A functions can be called using keyword arguments to specify the values of parameters.

def student(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

student(name="Naziya", age=22, city="Hyderabad")

student(city="Delhi", name="Rahul", age=25)




#---------------------------------------------------
#QUIZ 4
# USING *ARGS
# A function can accept a variable number of arguments using *args.

def total(*numbers):
    print("Sum:", sum(numbers))

total(10, 20, 30, 40)




#---------------------------------------------------
#QUIZ 5
# USING **KWARGS
# A function can accept a variable number of keyword arguments using **KWARGS.

def details(**data):
    for key, value in data.items():
        print(key, ":", value)

details(Name="Naziya", Age=22, City="Hyderabad")





#---------------------------------------------------
#QUIZ 6
# FLEXIBLE ARGUMNETS
# A flexible function performs different operations based on the input type of arguments.

def display(value):

    if isinstance(value, int):
        print("Square:", value * value)

    elif isinstance(value, str):
        print("Uppercase:", value.upper())

display(5)
display("python")





#---------------------------------------------------
#QUIZ 7
# ADVANCED FLEXIBLE ARGUMENTS
# A flexible function can accept both positional and keyword arguments using *args and **kwargs.

def bill(price=100, *items, **discount):

    total = price

    for item in items:
        total += item

    if "offer" in discount:
        total -= discount["offer"]

    print("Final Bill:", total)

bill(500, 100, 50, offer=70)




#---------------------------------------------------
#QUIZ 8
# LAMBDA FUNCTIONS
# A lambda function is an anonymous function that can have any number of arguments but only one expression.

add = lambda a, b: a + b

square = lambda x: x * x

print(add(10,20))

print(square(6))



#---------------------------------------------------
#QUIZ 9
# MAP FUNCTION
# The map() function applies a given function to all items in an iterable (list, tuple etc.) and returns a map object.

numbers = [1,2,3,4,5]

square = list(map(lambda x: x*x, numbers))

print(square)




#---------------------------------------------------
#QUIZ 10
# FILTER FUNCTIONS
# The filter() function filters the items in an iterable based on a given function and returns a filter object.

numbers = [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)