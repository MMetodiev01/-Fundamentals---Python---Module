initial_loot = input().split("|")

is_empty = False
while True:
    command = input()
    if command == "Yohoho!":
        break
    data = command.split()
    action = data[0]
    if action == 'Loot':
        for element in range(1, len(data)):
            if data[element] not in initial_loot:
                initial_loot.insert(0, data[element])
    elif action == 'Drop':
        index = int(data[1])
        if index < 0 or index >= len(initial_loot):
            continue
        element = initial_loot.pop(index)
        initial_loot.append(element)
    elif action == 'Steal':
        count_elements = int(data[1])
        if count_elements >= len(initial_loot):
            print(*initial_loot, sep=', ')
            is_empty = True
            break
        else:
            stolen_items = initial_loot[len(initial_loot) - count_elements:len(initial_loot) + 1]
            print(*stolen_items, sep=', ')
            del initial_loot[len(initial_loot) - count_elements:len(initial_loot) + 1]

if is_empty:
    print('Failed treasure hunt.')
else:
    length = 0
    for word in initial_loot:
        length += len(word)
    average_gain = length / len(initial_loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
