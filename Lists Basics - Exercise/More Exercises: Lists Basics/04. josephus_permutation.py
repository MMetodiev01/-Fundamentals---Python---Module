people_list = input().split()
number = int(input())

permutation = []
human_index = 0
counter = 0
while len(people_list) > 0:
    counter += 1
    if counter % number == 0:
        permutation.append(people_list[human_index])
        people_list.pop(human_index)
    else:
        human_index += 1
    if human_index >= len(people_list):
        human_index = 0
print('[' + ','.join(permutation) + ']')
