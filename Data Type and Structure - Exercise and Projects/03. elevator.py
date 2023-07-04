import math

number_of_people = int(input())
capacity = int(input())
final = math.ceil(number_of_people / capacity)
print(final)