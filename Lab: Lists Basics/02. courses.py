number = int(input())
# we are creating an empty list
lst_of_courses = []

# making for loop to go through as many times as is the number of input
for courses in range(number):
    # we read the current courses from input and added with append function in the list
    current_course = input()
    lst_of_courses.append(current_course)
# for final, we print the list
print(lst_of_courses)

# --------------------------------- 02. Courses ---------------------
# On the first line, you will receive a single number number. \
# On the following number lines, you will receive names of courses. You should create a list of courses and print it
# Inputs:
# 2
# PB Python
# PF Python
# --------
# 4
# Front-End
# C# Web
# JS Core
# Programming Fundamentals
# ---------
# Outpus:
# ['PB Python', 'PF Python']
# ['Front-End', 'C# Web', 'JS Core', 'Programming Fundamentals']