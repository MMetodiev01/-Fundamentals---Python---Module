# on the first line we receive input(str) with single space between the numbers(we use .split)
list_of_number = input().split()
# we make empty list for the opposite numbers that we need to print
opposite_list = []
# we make for loop to go through each element we receive with IN function
for element in list_of_number:
    # because we receive a string we cannot put only "-" in front of the number because if it is negative number it will not convert\
    # to a positive number, we must make it to integer
    current_number = -int(element)
    # after that we are adding it to the list
    opposite_list.append(current_number)
print(opposite_list)


# --------------------------------- 01. Invert Values ---------------------
# Write a program that receives a single string containing positive and negative numbers separated by a single space.\
# Print a list containing the opposite of each number.
# Inputs:
# 1 2 -3 -3 5
# -4 0 2 57 -101
# -------
# Outputs:
# [-1, -2, 3, 3, -5]
# [4, 0, -2, -57, 101]