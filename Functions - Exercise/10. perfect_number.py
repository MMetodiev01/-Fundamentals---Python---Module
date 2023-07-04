def perfect_number(number):
    # we make divisors list for the divisors
    divisors_list = []
    # boolean variable to see if the sum of the divisors list is equal to the given number
    is_perfect = False
    # for loop to go from 1 to the given number
    for current_number in range(1, number):
        # we ask if there is no remainder after the modular division and append the cur_num to the list
        if number % current_number == 0:
            divisors_list.append(current_number)
    # we ask if the sum of the divisors is equal to the given number and change the boolean to TRUE
    if sum(divisors_list) == number:
        is_perfect = True
    return is_perfect


num = int(input())
is_valid = perfect_number(num)
if is_valid:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

# --------------------------------- 10. Perfect Number ---------------------
# A perfect number is a positive integer that is equal to the sum of its proper positive divisors. \
# That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
# · "We have a perfect number!" - if the number is perfect.
# · "It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.

# Inputs:
# 6
# 28
# 1236498

# Outputs:
# We have a perfect number!  |  1 + 2 + 3
# We have a perfect number!  |   1 + 2 + 4 + 7 + 14
# It's not so perfect.
