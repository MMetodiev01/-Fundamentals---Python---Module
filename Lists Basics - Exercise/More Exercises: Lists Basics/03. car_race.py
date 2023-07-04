numbers_of_time = list(map(int, input().split()))

final_line = len(numbers_of_time) // 2
left_racer = numbers_of_time[:final_line]
right_racer = numbers_of_time[final_line:]

left_finish = 0
right_finish = 0

for index in range(numbers_of_time):
    left_car = left_racer[index]
    right_car = right_racer[index]
    if left_car == 0:
        left_finish *= 0.8
    if right_car == 0:
        right_finish *= 0.8
    left_finish += left_car
    right_finish += right_car
if left_finish < right_finish:
    print(f"The winner is left with total time: {left_finish:.1f}")
else:
    print(f"The winner is right with total time: {right_finish:.1f}")

# numbers_of_time = input().split()
# for time in numbers_of_time:
#     final_line = len(numbers_of_time) // 2
#     left_racer = numbers_of_time[:final_line]
#     right_racer = numbers_of_time[final_line:]
# result_left = []
# for x in left_racer:
#     result_left.append(int(x))
#     if int(x) == 0:
#         result_left.remove(int(x))
#         result_after_null_left = sum(result_left) * 0.2
# finish_time_left = sum(result_left) - result_after_null_left
#
# result_right = []
# for x in right_racer:
#     result_right.append(int(x))
#     if int(x) == 0:
#         result_right.remove(int(x))
#         result_after_null_right = sum(result_right) * 0.2
# finish_time_right = sum(result_right) - result_after_null_right
#
# if finish_time_left < finish_time_right:
#     print(f'The winner is left with total time: {finish_time_left:.1f}')
# else:
#     print(f'The winner is right with total time: {finish_time_right:.1f}')
