# we read the factor number and the count number from user
factor = int(input())
count = int(input())
# we make an empty list for the numbers we need to print
number_lst = []
# we make for loop in range(starting from 1 to count number + 1, because we need include that number)
for number in range(1, count + 1):
    # after that we can add the number from range and in brackets we can type what action must do
    number_lst.append(number * factor)
print(number_lst)


# --------------------------------- 02. Multiples List ---------------------
# Write a program that receives two numbers (factor and count).\
# It should create a list with a length of the given count that contains only integer numbers, which are multiples of the given factor.\
# The numbers should be only positive, and they should be arranged in ascending order, starting from the value of the factor.
# Inputs:
# 2
# 5
# ----
# 1
# 10
# -------
# Outputs:
# [2, 4, 6, 8, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
















# --------------------------------- 02. Multiples List ---------------------