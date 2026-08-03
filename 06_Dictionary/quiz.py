# CREATE A DICTIONARY 
# Dictionary stores data as key-value pairs 

students = {
    101: "Naaz",
    102: "Ayesha",
    103: "Zunaira",
    104: "Aman",
    105: "Shimalia"
}

print(students)


# ADDING NEW ENTRIES 
# New key-value pair can be added by assigning a value to a new key

students[106] = "Saifan"
students[107] = "Roman"

print(students)


# UPDATING EXISTING VALUES
# Assign a new vlaue to an existing key to update it

students[102] = "Fatima"

print(students)


# ACCESS VALUES
# values can be accessed using their keys

print("Student with ID 101:", students[101])

print("All Student Names:")
print(students.values())


# ITERATE THROUGH DICTIONARY
# Use a loop to access every key-value pair

for key, value in students.items():
    print(key, ":", value)


# PRINT ONLY KEYS 
# The keys() method returns all keys 

print("Student IDs")

for key in students.keys():
    print(key)


# PRINT ONLY VALUES
# The values() method returns all vslues

print("Student Names")

for value in students.values():
    print(value)


# CREATE A NESTED DICTIONARY
# Nested dictionary contains another dictionary as its values

students = {
    101: {"name": "Naaz", "age": 22},
    102: {"name": "Ayesha", "age": 21},
    103: {"name": "Zunaira", "age": 23}
}

print(students)


# ACCESS NESTED VALUES
# Nested values are accessed using multiple keys

print("Name:", students[101]["name"])
print("Age:", students[101]["age"])


# DELETE ELEMENTS
# Dictionary elements can be removes using del, pop(), or popitem()

# Delete using del 
del students[103]
print(students)

# Remove last inserted item 
students.popitem()
print(students)

# Remove using pop()
students.pop(101)
print(students)



#----------------------------------------------------
# QUIZ 2

# CHECK KEY EXISTENCE IN DICTIONARY
# The in operator can be used to check if a key exists in a dictionary

student_id = 102

if student_id in students:
    print("Student ID Found")
else:
    print("Student ID Not Found")



# ----------------------------------------------------
# QUIZ 3

# COUNT ENTRIES IN DICTIONARY
# The len() function can be used to count the number of entries in a dictionary

print("Total Students:", len(students))



#----------------------------------------------------
# QUIZ 4
# MERGE TWO DICTIONARIES
# Two dictionaries can be merged using the | operator or update()

students1 = {
    101: "Naaz",
    102: "Ayesha"
}

students2 = {
    103: "Zunaira",
    104: "Aman"
}

students1.update(students2)

print(students1)



#----------------------------------------------------
# QUIZ 5
# DICTIONARY COMPREHENSION
# Dictionary comprehension allows you to create a dictionary using a single line of code 
# or create a single line dictionary

squares = {num: num * num for num in range(1, 6)}

print(squares)



#-------------------------------------------------------
# QUIZ 6
# REVERSE DICTIONARY
# Reverse dictionary swaps keys and values

students = {
    101: "Naaz",
    102: "Ayesha",
    103: "Zunaira"
}

reverse = {}

for key, value in students.items():
    reverse[value] = key

print(reverse)