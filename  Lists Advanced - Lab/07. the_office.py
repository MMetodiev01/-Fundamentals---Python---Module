# Method *1 with Function Definition:
# 1. we make the first function to see how much is the increase happiness for each person
# ( we go through the list we make at the beginning and with each element from the list we multiply it with the happy factor)
def increase_happy(person, factor):
    increase_list = []
    for data in person:
        result = data * factor
        increase_list.append(result)
    return increase_list


# 2. we make another function to see how much people are happy from the list
# ( we take the list with multiplied elements and make if statement to see if the element is bigger\
#  than the sum of that list divided by the length of the same list)
def one_employee_happy(person, factor):
    happy_list = increase_happy(person, factor)
    one_person_list = []
    for data in happy_list:
        if data > sum(happy_list) / len(happy_list):
            one_person_list.append(data)
    return one_person_list


employees = list(map(int, input().split(' ')))
happy_factor = int(input())
character = one_employee_happy(employees, happy_factor)
# -------------------------------------------------------
# Method *2 with List Comprehension:
# employees = list(map(int, input().split(' ')))
# happy_factor = int(input())
# increase_happy = [data * happy_factor for data in employees]
# character = [data for data in increase_happy if data > sum(increase_happy) / len(increase_happy)]


if len(character) >= len(employees) // 2:
    print(f"Score: {len(character)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(character)}/{len(employees)}. Employees are not happy!")

# --------------------------------- 07. The Office ---------------------
# You will receive two lines of input:
# · a list of employees' happiness as a string of numbers separated by a single space
# · a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# · If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# · Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"

# Inputs:
# 1 2 3 4 2 1
# 3
# ----
# 2 3 2 1 3 3
# 4
# ---------
# Outputs:
# Score: 2/6. Employees are not happy!
# -----
# Score: 3/6. Employees are happy
