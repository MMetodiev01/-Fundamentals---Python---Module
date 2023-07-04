def odd_and_even(digit):
    # we make two variables to add the there each number and sum them
    sum_of_odd_numbers = 0
    sum_of_even_numbers = 0
    # we make for loop to go through each element of the string number we receive
    for item in digit:
        # then we make variable to convert the str days to integer
        element = int(item)
        if element % 2 == 0:
            sum_of_even_numbers += element
        else:
            sum_of_odd_numbers += element
    return sum_of_odd_numbers, sum_of_even_numbers


single_number_string = input()
sum_of_odd_digits, sum_of_even_digits = odd_and_even(single_number_string)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")

# --------------------------------- 04. Odd and Even Sum ---------------------
# You will receive a single number.\
# You should write a function that returns the sum of all even and all odd digits in a given number.\
# The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.

# Inputs:
# 1000435
#
# 3495892137259234

# Outputs:
# Odd sum = 9, Even sum = 4
#
# Odd sum = 54, Even sum = 22
