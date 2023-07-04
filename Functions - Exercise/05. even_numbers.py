def even_number(number):
    return number % 2 == 0


# we read our numbers from the input, and we use map function to go through every number and make it integer
numbers = list(map(int, input().split(' ')))
# after that we filter the result to see which number is even(gives TRUE) and we use lambda to use our function(even_number) on numbers
result = filter(lambda x: even_number(x), numbers)
print(list(result))

# numbers = list(map(int, input().split(' ')))
# final = filter(lambda x: x % 2 == 0, numbers)
# print(list(final))


# --------------------------------- 05. Even Numbers ---------------------
# Write a program that receives a sequence of numbers (integers) separated by a single space.\
# It should print a list of only the even numbers. Use filter().

# Inputs:
# 1 2 3 4
# 1 2 3 -1 -2 -3

# Outputs:
# [2, 4]
# [2, -2]
