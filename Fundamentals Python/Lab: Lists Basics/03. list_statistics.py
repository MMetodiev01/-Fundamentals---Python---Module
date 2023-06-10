
number_of_integers = int(input())
# we are making lists for 'positive' and 'negative' numbers to store them
positive_number_lst = []
negative_number_lst = []
# we are making for loop because we need to read current number as much as the number of integers
for number in range(number_of_integers):
    current_number = int(input())
    # after we read the first number we check if it is positive or negative with if statement whether the number is bigger then 0\
    # and added with append function in the relevant list
    if current_number > 0:
        positive_number_lst.append(current_number)
    else:
        negative_number_lst.append(current_number)
print(positive_number_lst)
print(negative_number_lst)
# we can check how many numbers are in the list by finding the length of the list
print(f'Count of positives: {len(positive_number_lst)}')
# we can add the sum of all number with 'sum' function
print(f'Sum of negatives: {sum(negative_number_lst)}')

# --------------------------------- 03. List Statistics ---------------------
# On the first line, you will receive a number number. On the following number lines, you will receive integers.\
# You should create and print two lists:
# · One with all the positives (including 0) numbers
# · One with all the negatives numbers
# Finally, print the following message:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"
# Inputs:
# 5
# 10
# 3
# 2
# -15
# -4
# ------
# 6
# 11
# 2
# 35
# 599
# 31
# 20
# ---------
# Outputs:
# [10, 3, 2]
# [-15, -4]
# Count of positives: 3
# Sum of negatives: -19
# [11, 2, 35, 599, 31, 20]
# []
# Count of positives: 6
# Sum of negatives: 0

