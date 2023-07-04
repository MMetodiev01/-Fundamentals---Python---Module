employee_1_efficiency = int(input())
employee_2_efficiency = int(input())
employee_3_efficiency = int(input())
students = int(input())
student_per_hour = employee_1_efficiency + employee_2_efficiency + employee_3_efficiency
total = students

hour = 0
while students > 0:
    hour += 1
    if hour % 4 == 0:
        continue
    else:
        total -= student_per_hour
print(f'Time needed: {hour}h.')
