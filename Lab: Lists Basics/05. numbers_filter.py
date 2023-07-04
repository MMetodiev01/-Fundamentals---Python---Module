
number_of_line = int(input())
# we are making constants(letters must be CAPITALS!!) for every category and list to add the numbers
COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_POSITIVE = 'positive'
COMMAND_NEGATIVE = 'negative'

number_lst = []
for _ in range(number_of_line):
    current_number = int(input())
    number_lst.append(current_number)
# after we read the numbers and added in the list we read the following command and make a list\
# for filtered numbers
command = input()
filtered_number = []
# we go through every number with for loop IN the list
for number in number_lst:
    # we check if our constant is equal to the command we receive and if the number answer the criteria
    filtered_passes = (
        (command == COMMAND_EVEN and number % 2 == 0) or
        (command == COMMAND_ODD and number % 2 != 0) or
        (command == COMMAND_POSITIVE and number >= 0) or
        (command == COMMAND_NEGATIVE and number < 0)
    )
    # after checking the command and the criteria we check if the command and the criteria is TRUE, if it is \
    # we add the number in list(filtered_number)
    if filtered_passes:
        filtered_number.append(number)
print(filtered_number)

# --------------------------------- 05. Numbers Filter ---------------------
# On the first line, you will receive a single number number. On the following number lines, you will receive integers.\
# After that, you will be given one of the following commands:
# · even
# · odd
# · negative
# · positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.
# Inputs:
# 5
# 33
# 19
# -2
# 18
# 998
# even
# -------
# 3
# 111
# -4
# 0
# negative
# --------
# Outputs:
# [-2, 18, 998]
# [-4]