targets = list(map(int, input().split()))
while True:
    command = input()
    if command == 'End':
        break
    data = command.split()
    input_data = data[0]
    data_index = int(data[1])
    number = int(data[2])
    if input_data == 'Shoot' and 0 <= data_index < len(targets):
        power = number
        if targets[data_index] - power > 0:
            targets[data_index] -= power
        else:
            del targets[data_index]
    elif input_data == 'Add':
        value = number
        if data_index < 0 or data_index >= len(targets):
            print("Invalid placement!")
        else:
            targets.insert(data_index, value)
    elif input_data == 'Strike':
        radius = number
        if data_index - radius < 0 or data_index + radius >= len(targets):
            print("Strike missed!")
        else:
            del targets[data_index - radius:data_index + radius + 1:]
print(*targets, sep="|")
