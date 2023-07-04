initial_list = input().split('!')

while True:
    command = input()
    if command == "Go Shopping!":
        break
    data = command.split()
    action = data[0]
    item = data[1]
    if action == 'Urgent':
        if item in initial_list:
            continue
        else:
            initial_list.insert(0, item)
    elif action == "Unnecessary":
        if item in initial_list:
            initial_list.remove(item)
    elif action == "Correct":
        new_item = data[2]
        if item in initial_list:
            element = initial_list.index(item)
            initial_list.remove(item)
            initial_list.insert(element, new_item)
    elif action == "Rearrange":
        if item in initial_list:
            element = initial_list.index(item)
            initial_list.remove(item)
            initial_list.append(item)
print(*initial_list, sep=", ")
