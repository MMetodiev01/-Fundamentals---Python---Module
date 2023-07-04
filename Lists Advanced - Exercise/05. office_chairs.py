def check_the_rooms(rooms):
    # we are making two variables to safe how much chairs and visitors is in the room
    total_chairs = 0
    total_visitor = 0
    # we go through every room
    for room in range(1, rooms + 1):
        # we read the input and split it to make chairs and visitors
        free_chairs, visitors = input().split(' ')
        # then we subtract from the length of the chairs to int the visitors(they are string in the beginning
        left = len(free_chairs) - int(visitors)
        # then if the chairs is more we add to the variable and others to other variable
        if left >= 0:
            total_chairs += left
        else:
            # because is negative number we make them positive with abs function
            total_visitor += abs(left)
            print(f"{abs(left)} more chairs needed in room {room}")
    return total_chairs, total_visitor


number_of_rooms = int(input())
total_free_chairs, needed_chairs = check_the_rooms(number_of_rooms)
if total_free_chairs >= needed_chairs:
    print(f'Game On, {total_free_chairs} free chairs left')

# --------------------------------- 05. Office Chairs ---------------------
# You are a facility manager at a large business center.
# One of your responsibilities is to check if each conference room in the center has enough chairs for the visitors.
# On the first line, you will be given an integer n representing the number of rooms in the business center.
# On the following n lines for each room, you will receive information about the chairs in the room and the number of visitors.
# Each chair will be presented with the char "X".
# Next, there will be a single space and the number of visitors at the end. For example: "XXXXX 4" (5 chairs and 4 visitors).
# Keep track of the free chairs:
# · If there are not enough chairs in a specific room,
# print the following message: "{needed_chairs_in_room} more chairs needed in room {number_of_room}". The rooms start from 1.
# · Otherwise, print: "Game On, {total_free_chairs} free chairs left".

# Inputs:
# 4
# XXXX 4
# XX 1
# XXXXXX 3
# XXX 3
# -------
# 3
# XXXXXXX 5
# XXXX 5
# XXXXXX 8

# Outputs:
# Game On, 4 free chairs left
# ------
# 1 more chairs needed in room 2
# 2 more chairs needed in room 3
