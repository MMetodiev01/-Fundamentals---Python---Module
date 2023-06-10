def palindrome_number(digit):
    check_list = []
    for numbers in digit:
        if numbers == numbers[::-1]:
            check_list.append("True")
        else:
            check_list.append("False")
    return check_list


number = input().split(", ")
print('\n'.join(palindrome_number(number)))
# --------------------------------- 08. Palindrome Integers ---------------------
# A palindrome is a number that reads the same backward as forward, such as 323 or 1001.\
# Write a function that receives a list of positive integers, separated by comma and space ", ".\
# The function should check if each integer is a palindrome - True or False. Print the result.

# Inputs:
# 123, 323, 421, 121
# 32, 2, 232, 1010

# Outputs:
# False True False True
# False True True False
