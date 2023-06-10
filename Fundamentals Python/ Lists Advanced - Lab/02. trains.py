number = int(input())
# we first take the count of the wagons and automatically create the number of wagons
wagon = [0] * number

while True:
    # in the beginning we receive commands the first command we receive we won't split it\
    # to see if it's equal to 'End'
    command = input()
    if command == 'End':
        break
    # if the command it's not equal to 'End' then we split it ,and we will receive a list that contains other things
    split_command = command.split(' ')
    # the first thing on the list is the action (what to do) wit that action
    action = split_command[0]
    # we make if statement to see if the action is 'add', 'insert' or 'leave'
    if action == 'add':
        # on the 'add' action the second thing we receive from the split command is the 'people' that\
        # need to be 'add' on the last wagon and we the people from str to int (and that's include for the other actions)
        people = int(split_command[1])
        wagon[-1] += people
    elif action == 'insert':
        wagon_index = int(split_command[1])
        people_in = int(split_command[2])
        wagon[wagon_index] += people_in
    elif action == 'leave':
        wagon_index = int(split_command[1])
        people_out = int(split_command[2])
        wagon[wagon_index] -= people_out
print(wagon)

# --------------------------------- 02. Trains---------------------
# You will receive a number representing the number of wagons a train has.\
# Create a list (train) with the given length containing only zeros. Until you receive the command "End",\
# you will receive some of the following commands:
# · "add {people}" – you should add the number of people in the last wagon
# · "insert {index} {people}" - you should add the number of people at the given wagon
# · "leave {index} {people}" - you should remove the number of people from the wagon.\
# There will be no case in which the people will be more than the count in the wagon.
# There will be no case in which the index is invalid!
# After you receive the "End" command print the train.

# Inputs:
# 3
# add 20
# insert 0 15
# leave 0 5
# End
# -----------
# 5
# add 10
# add 20
# insert 0 16
# insert 1 44
# leave 1 12
# insert 2 100
# insert 4 61
# leave 4 1
# add 15
# End
# -----------
# Outputs:
# [10, 0, 20]
# [16, 32, 100, 0, 105]
