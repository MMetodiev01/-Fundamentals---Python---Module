tasks = []

while True:
    command = input()
    if command == 'End':
        break
    split_command = command.split('-')
    priority = int(split_command[0])
    to_do_task = split_command[1]

    tasks.append((priority, to_do_task))
# we go through the 'tasks' list ,but we sorted it because we append the priority there and when we use sorted function the priority\
# will be sorted from the smallest to biggest along with the current_task
# final_result = [data[1] for data in sorted(tasks)]
final_result = []
for data in sorted(tasks):
    final_result.append(data[1])
print(final_result)

# --------------------------------- 03. To-do List ---------------------
# You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive).
# Hint: · Use the pop() and insert() methods.

# Inputs:        |  Outputs:
# 2-Walk the dog    ['Drink coffee', 'Walk the dog', 'Work', 'Dinner']
# 1-Drink coffee
# 6-Dinner
# 5-Work
# End
# ----------
# 3-C            |  ['B', 'A', 'C', 'V']
# 2-A
# 1-B
# 6-V
# End
