def positive_numbers(nums):
    return [num for num in nums if int(num) >= 0]


def negative_numbers(nums):
    return [num for num in nums if int(num) < 0]


def odd_numbers(nums):
    return [num for num in nums if int(num) % 2 != 0]


def even_numbers(nums):
    return [num for num in nums if int(num) % 2 == 0]


numbers = input().split(", ")
print(f"Positive: {', '.join(positive_numbers(numbers))}")
print(f"Negative: {', '.join(negative_numbers(numbers))}")
print(f"Even: {', '.join(even_numbers(numbers))}")
print(f"Odd: {', '.join(odd_numbers(numbers))}")

# --------------------------------- 04. Number Classification ---------------------
# Using a list comprehension, write a program that receives numbers,\
# separated by comma and space ", ", and prints all the positive, negative, even, and odd numbers\
# on separate lines as shown below.

# Inputs:
# 1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33
# 1, 2, 53, 2, 21

# Outputs:
# Positive: 1, 0, 5, 3, 4, 12, 19
# Negative: -2, -100, -20, -33
# Even: -2, 0, 4, -100, -20, 12
# Odd: 1, 5, 3, 19, -33
# ------
# Positive: 1, 2, 53, 2, 21
# Negative:
# Even: 2, 2
# Odd: 1, 53, 21
