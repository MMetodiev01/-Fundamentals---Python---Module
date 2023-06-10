def factorial(number):
    for current_number in range(1, number):
        number *= current_number
    return number


first_number = int(input())
second_number = int(input())
first_factorial = factorial(first_number)
second_factorial = factorial(second_number)
final_result = first_factorial / second_factorial
print(f'{final_result:.2f}')

# --------------------------------- 12. Factorial Division ---------------------
# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point

# Inputs:
# 5
# 2
# ------
# 6
# 2
# ------
# Outputs:
# 60.00
# 360.00
