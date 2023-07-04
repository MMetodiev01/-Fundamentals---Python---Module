number = input().split()
counts_remove_number = int(input())
number_as_digits = []
final_list = []
for current_number in number:
    number_as_digits.append(int(current_number))
for _ in range(counts_remove_number):
    number_as_digits.remove(min(number_as_digits))
print(*number_as_digits, sep=", ")


# --------------------------------- 05. Faro Shuffle ---------------------
# Write a program that receives a list of integer numbers (separated by a single space) and a number number.
# The number number represents the count of numbers to remove from the list.
# You should remove the smallest ones, and then, you should print all the numbers that are left in the list, separated by a comma and a space ", ".

# Inputs:
# 10 9 8 7 6 5
# 3
# 1 10 2 9 3 8
# 2
# ----------------
# Outputs:
# 10, 9, 8
# 10, 9, 3, 8