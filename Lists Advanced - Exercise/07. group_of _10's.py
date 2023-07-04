def age(digits):
    grow = 10
    while len(digits) > 0:
        age_list = []
        for index, value in enumerate(digits):
            if value <= grow:
                age_list.append(digits.pop(index))
                digits.insert(index, 0)
        print(f'Group of {grow}\'s: {age_list}')
        digits = [num for num in digits if num != 0]
        if len(digits) == 0:
            break
        grow += 10


numbers = list(map(int, input().split(", ")))
age(numbers)
# --------------------------------- 07. Group of 10's ---------------------
# Write a program that receives a sequence of numbers (a string containing integers separated by ", ")\
# and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
# · The numbers 2, 8, 4, and 10 fall into the group of 10's.
# · The numbers 13, 19, 14, and 15 fall into the group of 20's.
# For more clarification, see the examples below.


# Inputs:
# 8, 12, 38, 3, 17, 19, 25, 35, 50
# -------
# 1, 3, 3, 4, 34, 35, 25, 21, 33

# Outputs:
# Group of 10's: [8, 3]
# Group of 20's: [12, 17, 19]
# Group of 30's: [25]
# Group of 40's: [38, 35]
# Group of 50's: [50]
# --------
# Group of 10's: [1, 3, 3, 4]
# Group of 20's: []
# Group of 30's: [25, 21]
# Group of 40's: [34, 35, 33]
