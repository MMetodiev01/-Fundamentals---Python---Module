def min_max_sum_numbers(number):
    min_number = min(number)
    max_number = max(number)
    sum_of_digits = sum(number)
    return f"The minimum number is {min_number}\nThe maximum number is {max_number}\nThe sum number is: {sum_of_digits}"


numbers = list(map(int, input().split(' ')))
print(min_max_sum_numbers(numbers))

# Example 2:
# numbers = list(map(int, input().split()))
# print(f"The minimum number is {min(numbers)}")
# print(f"The maximum number is {max(numbers)}")
# print(f"The sum number is: {sum(numbers)}")


# --------------------------------- 07. Min Max and Sum ---------------------
# Write a program that receives a sequence of numbers (integers) separated by a single space.\
# It should print the min and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
#
# The output should be as follows:
#
# · On the first line: "The minimum number is {minimum number}"
#
# · On the second line: "The maximum number is {maximum number}"
#
# · On the third line: "The sum number is: {sum of all numbers}"

# Inputs:
# 2 4 6
# 12 52 11 53 2 8 45


# Outputs:
# The minimum number is 2
# The maximum number is 6
# The sum number is: 12
# ---------
# The minimum number is 2
# The maximum number is 53
# The sum number is: 183
