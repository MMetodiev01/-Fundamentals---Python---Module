numbers = list(map(int, input().split(', ')))
index = [data for data in range(len(numbers)) if numbers[data] % 2 == 0]
print(index)
# we make the given number from str to int with map function
# we go through that list with integers with for loop in range the length of list and see if the list[index] is\
# even or odd

# --------------------------------- 06. Even Numbers ---------------------
# Write a program that reads a single string with numbers separated by comma and space ", ".\
# Print the indices of all even numbers.

# Input:
# 3, 2, 1, 5, 8
# 2, 4, 6, 9, 10
# ---------
# Output:
# [1, 4]
# [0, 1, 2, 4]