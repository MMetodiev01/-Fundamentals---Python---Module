import math

number_of_students = int(input())
total_lectures = int(input())
additional_bonus = int(input())
attended = 0
max_bonus = 0
for i in range(1, number_of_students + 1):
    school_visit = int(input())
    total_bonus = school_visit / total_lectures * (5 + additional_bonus)
    if max_bonus < total_bonus:
        max_bonus = total_bonus
        attended = school_visit
print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {attended} lectures.")
