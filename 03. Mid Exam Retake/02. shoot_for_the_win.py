# numbers_of_targets = list(map(int, input().split()))
#
# targets_count = 0
#
# while True:
#     command = input()
#     if command == 'End':
#         break
#     data_index = int(command)
#     for index, value in enumerate(numbers_of_targets):
#         if data_index == index:
#             targets_count += 1
#             current_target = numbers_of_targets.pop(index)
#             numbers_of_targets.insert(index, -1)
#             for x in range(len(numbers_of_targets)):
#                 if numbers_of_targets[x] == -1:
#                     continue
#                 elif numbers_of_targets[x] > current_target:
#                     numbers_of_targets[x] -= current_target
#                 elif numbers_of_targets[x] <= current_target:
#                     numbers_of_targets[x] += current_target
# numbers_of_targets = [str(x) for x in numbers_of_targets]
# print(f"Shot targets: {targets_count} -> {' '.join(numbers_of_targets)}")

# --------------- Example 2 --------------------- #
def reduce_values(target_sequence, index):
    special_value = target_sequence[index]
    target_sequence[index] = -1

    for i in range(len(target_sequence)):
        if target_sequence[i] == -1:
            continue
        if special_value < target_sequence[i]:
            target_sequence[i] -= special_value
        else:
            target_sequence[i] += special_value

    return target_sequence


def shoot_for_the_win_func(target_sequence):
    count_of_shot_targets = 0

    while True:
        command = input()
        if command == 'End':
            break
        index = int(command)
        if 0 <= index < len(target_sequence) and target_sequence[index] != -1:
            count_of_shot_targets += 1
            reduce_values(target_sequence, index)
    convert_values = [str(x) for x in target_sequence]
    print(f"Shot targets: {count_of_shot_targets} -> {' '.join(convert_values)}")


data = list(map(int, input().split(' ')))
shoot_for_the_win_func(data)
