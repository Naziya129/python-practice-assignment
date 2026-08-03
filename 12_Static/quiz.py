# QUIZ 1
# DEFINE ANS ACCESS VIA CLASS
# A class variable is shared by all objects of a class and is defined inside the class but outside any methods.

class Student:

    college = "SVIT"

print(Student.college)



#--------------------------------------------------
# QUIZ 2
# ACCESS VIA OBJECT (INSTANCE)
# A class variable can also be accessed through an object (instance) of the class.

class Student:

    college = "SVIT"

student = Student()

print(student.college)



#--------------------------------------------
# QUIZ 3
# MODIFY CLASS VARIABLE VIA INSTANCE
#Modifying a class variable through an instance creates an instance variable with the same name.

class Student:

    college = "SVIT"

student = Student()

student.college = "ABC College"

print("Using Instance:", student.college)

print("Using Class:", Student.college)





#--------------------------------------------
# QUIZ 4
# MODIFY CLASS VARIABLE VIA CLASS
# Modifying a class variable using the class name updates it for all objects that have not overridden it.

class Student:

    college = "SVIT"

student1 = Student()

student2 = Student()

Student.college = "Python Institute"

print("Using Class:", Student.college)

print("Student1:", student1.college)

print("Student2:", student2.college)




#--------------------------------------------
# QUIZ 5
# CLASS VARIABLE VS INSTANSE VARIABLE
# A class variable is shared by all objects, while an instance variable belongs to each individual object.

class Student:

    college = "SVIT"      # Class Variable

    def __init__(self, name):
        self.name = name          # Instance Variable

student1 = Student("Naaz")

student2 = Student("Aisha")

print("Student 1 Name:", student1.name)

print("Student 2 Name:", student2.name)

print("College:", Student.college)

print("Student 1 College:", student1.college)

print("Student 2 College:", student2.college)




#--------------------------------------------
# QUIZ 6
# SHARED COUNTER PROGRAM
# A class variable can keep track of information shared by all objects, such as the total number of objects created.

class Student:

    count = 0

    def __init__(self, name):

        self.name = name

        Student.count += 1

        print(self.name, "Object Created")

student1 = Student("Naaz")

student2 = Student("Aisha")

student3 = Student("Sara")

print("Total Students:", Student.count)




#--------------------------------------------
# QUIZ 7
# CONFIGURATION SETTING EXAMPLE
# A class variable can act as a shared configuration that is common to all objects.

class Course:

    course_name = "Python Basics"

course1 = Course()

course2 = Course()

print("Course 1:", course1.course_name)
print("Course 2:", course2.course_name)

Course.course_name = "Full Stack Python"

print()

print("After Updating Configuration")

print("Course 1:", course1.course_name)
print("Course 2:", course2.course_name)
print("Class:", Course.course_name)