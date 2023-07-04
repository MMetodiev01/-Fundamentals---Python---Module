rooms = input().split("|")
bitcoins = 0
initial_health = 100

count_rooms = 0
is_dead = False
while True:
    for data in rooms:
        command = data.split(' ')
        action = command[0]
        number = int(command[1])
        count_rooms += 1
        if action == "potion":
            if initial_health + number > 100:
                diff = 100 - initial_health
                print(f"You healed for {diff} hp.")
                initial_health = 100
            else:
                initial_health += number
                print(f"You healed for {number} hp.")
            print(f"Current health: {initial_health} hp.")
        elif action == "chest":
            bitcoins += number
            print(f"You found {number} bitcoins.")
        else:
            if initial_health - number > 0:
                initial_health -= number
                print(f"You slayed {action}.")
            else:
                print(f"You died! Killed by {action}.")
                print(f"Best room: {count_rooms}")
                is_dead = True
                break
    break
if not is_dead:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {initial_health}")
