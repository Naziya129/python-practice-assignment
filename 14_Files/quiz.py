# QUIZ 1
# READ A TEXT FILE
# A text file opened in 'r' mode is used to read the contents.
#---

#file = open("sample.txt", "r")

#content = file.read()

#print(content)

#file.close()



#---------------------------------------------------
# quiz 2
# WRITE TO A TEXT FILE 
# 'w' mode creates/overwrites a file, while 'a' mode appends data to the end of a file.

text = input("Enter text: ")

file = open("sample.txt", "w")
file.write(text)
file.close()

file = open("sample.txt", "a")
file.write("\nThank You")
file.close()

print("Data Written Successfully")




#---------------------------------------------------
# quiz 3
# READ FILE USING FILE OBJECT
# read(), readline(), and readlines() read file contents in diff ways.

file = open("sample.txt", "r")

print("Using read()")
print(file.read())

file.close()

file = open("sample.txt", "r")

print("Using readline()")
print(file.readline())

file.close()

file = open("sample.txt", "r")

print("Using readlines()")
print(file.readlines())

file.close()




#---------------------------------------------------
# quiz 4
# RANDOM ACCESS FILE READING
# seek() moves the file pointer to a specified position.

file = open("sample.txt", "r")

file.seek(6)

print(file.read())

file.close()




#---------------------------------------------------
# quiz 5
# READ FROM A SPECIFIC INDEX
# seek() changes the cursor positions and read(n) reads a fixed number of characters.

file = open("sample.txt", "r")

file.seek(6)

print(file.read(10))

file.close()





#---------------------------------------------------
# quiz 6
# CHECK FILE PERMISSIONS
# os.access() checks whether a file has specific permissions.

import os

filename = "sample.txt"

print("Read Permission :", os.access(filename, os.R_OK))

print("Write Permission:", os.access(filename, os.W_OK))





#---------------------------------------------------
# quiz 7
# COUNT WORDS, LINES AND CHARACTERS
# A file cna be analyzed to count its lines, words and characters.

file = open("sample.txt", "r")

content = file.read()

lines = content.split("\n")
words = content.split()

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(content))

file.close()



#---------------------------------------------------
# quiz 8
# COPY FILE COMTENT
# A file can be copied by reading from one file and writing to another.
 
source = open("sample.txt", "r")

destination = open("copy.txt", "w")

destination.write(source.read())

source.close()

destination.close()

print("File Copied Successfully")




#---------------------------------------------------
# quiz 9
# APPEND DATA WITH TIMESTAMP
# The 'datetime' module is used to write the current data and time to a file.

from datetime import datetime

file = open("sample.txt", "a")

file.write("\n")

file.write(str(datetime.now()))

file.close()

print("Timestamp Added Successfully")


