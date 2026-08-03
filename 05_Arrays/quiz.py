# QUIZ 1
# SUM OF ELEMENTS
# The sum of a list is the total obtained by adding all its elements.

def sum_list(numbers):

    total = 0

    for num in numbers:
        total += num

    return total

list1 = [10, 20, 30, 40, 50]

print("Sum:", sum_list(list1))




#----------------------------------------------------
# QUIZ 2
# AVERAGE OF ELEMENTS
# The average is the sum of all elements divided by the total number of elements.

def average_list(numbers):

    total = 0

    count = 0

    for num in numbers:
        total += num
        count += 1

    return total / count

list1 = [10, 20, 30, 40, 50]

print("Average:", average_list(list1))




#----------------------------------------------------
# QUIZ 3
# FIND INDEX OF AN ELEMENT
# The index is the position of an element in a list.

def find_index(numbers, value):

    for i in range(len(numbers)):

        if numbers[i] == value:
            return i

    return -1

list1 = [10, 20, 30, 40, 50]

element = 30

index = find_index(list1, element)

if index != -1:
    print("Element Found at Index:", index)

else:
    print("Element Not Found")





#----------------------------------------------------
# QUIZ 4
# CHECK ELEMENTS PRESENCE
# The in operator checks whether an element exists in a list.

def check_element(numbers, value):

    if value in numbers:
        return True

    return False

list1 = [10, 20, 30, 40]

print(check_element(list1, 20))

print(check_element(list1, 60))



#----------------------------------------------------
# QUIZ 5
# REMOVE AN ELEMENT
# remove() deletes the first occurrence of a specified element from a list.

def remove_element(numbers, value):

    if value in numbers:
        numbers.remove(value)

    return numbers

list1 = [10, 20, 30, 40, 50]

print(remove_element(list1, 30))





#----------------------------------------------------
# QUIZ 6
# COPY A LIST
# Copying a list creates a new list containing the same elements as the original list.

def copy_list(original):

    new_list = []

    for item in original:
        new_list.append(item)

    return new_list

list1 = [10, 20, 30, 40, 50]

list2 = copy_list(list1)

print("Original List:", list1)

print("Copied List:", list2)





#----------------------------------------------------
# QUIZ 7
# INSERT ELEMENTS AT POSITION
# insert() adds an element at a specified index in a list.

def insert_element(numbers, index, value):

    numbers.insert(index, value)

    return numbers

list1 = [10, 20, 40, 50]

print(insert_element(list1, 2, 30))





#----------------------------------------------------
# QUIZ 8
# FIND MINIMUM AND MAXIMUM
# Minimum is the smallest element, and maximum is the largest element in a list.

def find_min_max(numbers):

    minimum = numbers[0]
    maximum = numbers[0]

    for num in numbers:

        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

    return minimum, maximum

list1 = [45, 12, 89, 23, 67]

minimum, maximum = find_min_max(list1)

print("Minimum:", minimum)

print("Maximum:", maximum)





#----------------------------------------------------
# QUIZ 9
# REVERSE A LIST
# Reversing a list changes the order of elements from last to first.

def reverse_list(numbers):

    reversed_list = []

    for i in range(len(numbers)-1, -1, -1):
        reversed_list.append(numbers[i])

    return reversed_list

list1 = [10, 20, 30, 40, 50]

print(reverse_list(list1))





#----------------------------------------------------
# QUIZ 10
# FIND DUPLICATE ELEMENTS
# Duplicate elements are values that appear more than once in a list.

def find_duplicates(numbers):

    duplicates = []

    for i in range(len(numbers)):

        count = 0

        for j in range(len(numbers)):

            if numbers[i] == numbers[j]:
                count += 1

        if count > 1 and numbers[i] not in duplicates:
            duplicates.append(numbers[i])

    return duplicates

list1 = [10, 20, 30, 20, 40, 10, 50]

print("Duplicate Elements:", find_duplicates(list1))




#----------------------------------------------------
# QUIZ 11
# COUNT EVEN AND ODD NUMBERS
# Even numbers are divisible by 2, while odd numbers are not.

def count_even_odd(numbers):

    even = 0
    odd = 0

    for num in numbers:

        if num % 2 == 0:
            even += 1

        else:
            odd += 1

    print("Even Numbers:", even)
    print("Odd Numbers:", odd)

list1 = [10, 15, 20, 25, 30, 35]

count_even_odd(list1)




#----------------------------------------------------
# QUIZ 12
# COMMON ELEMENTS BETWEEN TWO LISTS
# Common elements are values that exist in both lists.

def common_elements(list1, list2):

    common = []

    for item in list1:

        if item in list2 and item not in common:
            common.append(item)

    return common

list1 = [10, 20, 30, 40]

list2 = [30, 40, 50, 60]

print("Common Elements:", common_elements(list1, list2))




#----------------------------------------------------
# QUIZ 13
# REMOVE DUPLICATE
# Removing duplicates keeps only one occurrence of each element.

def remove_duplicates(numbers):

    unique = []

    for num in numbers:

        if num not in unique:
            unique.append(num)

    return unique

list1 = [10, 20, 10, 30, 20, 40, 50]

print(remove_duplicates(list1))




#----------------------------------------------------
# QUIZ 14
# SECOND LARGEST ELEMENTS
# The second largest element is the largest value after the maximum value.

def second_largest(numbers):

    largest = numbers[0]
    second = numbers[0]

    for num in numbers:

        if num > largest:
            second = largest
            largest = num

        elif num > second and num != largest:
            second = num

    return second

list1 = [10, 50, 80, 30, 70]

print("Second Largest:", second_largest(list1))




#----------------------------------------------------
# QUIZ 15
# DIFFERENCE BETWEEN MAX & MIN
# The difference is obtained by subtracting the minimum value from the maximum value.

def difference(numbers):

    minimum = numbers[0]
    maximum = numbers[0]

    for num in numbers:

        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

    return maximum - minimum

list1 = [15, 5, 25, 35, 45]

print("Difference:", difference(list1))





#----------------------------------------------------
# QUIZ 16
# CHECK FOR SPECIFIC ELEMENTS (12 AND 23)
# The in operator checks whether specific elements exist in a list.

def check_elements(numbers):

    if 12 in numbers and 23 in numbers:
        print("Both 12 and 23 are present.")

    else:
        print("Both elements are not present.")

list1 = [5, 12, 18, 23, 40]

check_elements(list1)





#----------------------------------------------------
# QUIZ 17
# UNOIQUE ELEMENTS ONLY
# A unique list contains each element only once.

def unique_elements(numbers):

    unique = []

    for num in numbers:

        if num not in unique:
            unique.append(num)

    return unique

list1 = [10, 20, 10, 30, 20, 40, 50]

print("Unique List:", unique_elements(list1))




#----------------------------------------------------
# QUIZ 18
# FREQUENCY COUNT
# Frequency is the number of times an element appears in a list.

def frequency(numbers):

    counted = []

    for num in numbers:

        if num not in counted:

            count = 0

            for item in numbers:

                if item == num:
                    count += 1

            print(num, ":", count)

            counted.append(num)

list1 = [10, 20, 10, 30, 20, 20, 40]

frequency(list1)




#----------------------------------------------------
# QUIZ 19
# LIST SORTING WITHOUT BUILT-IN FUNCTIONS
# Sorting arranges elements in ascending or descending order without using sort() or sorted().

def sort_list(numbers):

    n = len(numbers)

    for i in range(n):

        for j in range(i + 1, n):

            if numbers[i] > numbers[j]:

                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp

    return numbers

list1 = [45, 12, 89, 23, 5]

print("Sorted List:", sort_list(list1))




#----------------------------------------------------
# QUIZ 20
# MERGE TWO LISTS WITHOUT DUPLICATES
# Merging combines two lists while removing duplicate elements.

def merge_lists(list1, list2):

    merged = []

    for item in list1:

        if item not in merged:
            merged.append(item)

    for item in list2:

        if item not in merged:
            merged.append(item)

    return merged

list1 = [10, 20, 30, 40]

list2 = [30, 40, 50, 60]

print("Merged List:", merge_lists(list1, list2))


