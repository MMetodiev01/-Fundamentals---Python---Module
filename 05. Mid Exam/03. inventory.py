def inventory_func(items):
    while True:
        command = input()
        if command == 'Craft!':
            break
        data = command.split(' - ')
        action = data[0]
        item = data[1]
        if action == 'Collect':
            if item not in items:
                items.append(item)
        elif action == 'Drop':
            if item in items:
                items.remove(item)
        elif action == 'Combine Items':
            new_items = item.split(':')
            old_item = new_items[0]
            new_item = new_items[1]
            if old_item in items:
                index = items.index(old_item)
                items.insert(index + 1, new_item)
        elif action == 'Renew':
            if item in items:
                index_element = items.index(item)
                element = items.pop(index_element)
                items.append(element)
    print(*items, sep=', ')


inventory = input().split(", ")
inventory_func(inventory)

# ------------- Example 2 ---------- #
# inventory = input().split(", ")
#
# while True:
#     command = input()
#     if command == 'Craft!':
#         break
#     data = command.split(' - ')
#     action = data[0]
#     item = data[1]
#     if action == 'Collect':
#         if item not in inventory:
#             inventory.append(item)
#     elif action == 'Drop':
#         if item in inventory:
#             inventory.remove(item)
#     elif action == 'Combine Items':
#         new_items = item.split(':')
#         old_item = new_items[0]
#         new_item = new_items[1]
#         if old_item in inventory:
#             index = inventory.index(old_item)
#             inventory.insert(index + 1, new_item)
#     elif action == 'Renew':
#         if item in inventory:
#             index_element = inventory.index(item)
#             element = inventory.pop(index_element)
#             inventory.append(element)
# print(*inventory, sep=', ')
