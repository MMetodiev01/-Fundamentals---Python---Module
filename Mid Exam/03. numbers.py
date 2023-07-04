numbers = list(map(int, input().split()))
average_number = sum(numbers) / len(numbers)
bigger_number_list = [x for x in numbers if x > average_number]
bigger_number_list.sort(reverse=True)
if len(bigger_number_list) < 1:
    print("No")
else:
    print(*bigger_number_list[:5])
