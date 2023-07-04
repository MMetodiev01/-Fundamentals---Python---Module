number = int(input())

for num in range(1, number + 1):
    str_number = str(num)
    sum_list = []
    for i in str_number:
        sum_list.append(i)
    sum_list = [int(x) for x in sum_list]
    if sum(sum_list) == 5 or sum(sum_list) == 7 or sum(sum_list) == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
