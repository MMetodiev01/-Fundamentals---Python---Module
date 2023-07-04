numbers = list(map(int, input().split()))

while True:
    command = input()
    if command == 'end':
        break
    data = command.split()
    action = data[0]
    if action == 'swap':
        index_1 = int(data[1])
        index_2 = int(data[2])
        numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]
    elif action == 'multiply':
        index_1 = int(data[1])
        index_2 = int(data[2])
        result = numbers[index_1] * numbers[index_2]
        numbers[index_1] = result
    elif action == 'decrease':
        for i in range(len(numbers)):
            numbers[i] -= 1
print(*numbers, sep=', ')
