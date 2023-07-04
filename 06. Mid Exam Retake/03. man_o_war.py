pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
section_health = int(input())

destroyed = False
battle_finished = False
while True:
    command = input()
    if command == 'Retire':
        battle_finished = True
        break
    data = command.split()
    action = data[0]
    if action == "Fire":
        index = int(data[1])
        damage = int(data[2])
        if index < 0 or index >= len(warship):
            continue
        if warship[index] - damage <= 0:
            print(f"You won! The enemy ship has sunken.")
            break
        else:
            warship[index] -= damage
    elif action == 'Defend':
        start_index = int(data[1])
        end_index = int(data[2])
        damage = int(data[3])
        if start_index >= 0 and start_index < len(pirate_ship):
            if end_index >= 0 and end_index < len(pirate_ship):
                for ship_block in range(start_index, end_index + 1):
                    if pirate_ship[ship_block] - damage <= 0:
                        print(f"You lost! The pirate ship has sunken.")
                        destroyed = True
                        break
                    pirate_ship[ship_block] -= damage
    elif action == 'Repair':
        index = int(data[1])
        repair = int(data[2])
        if index >= 0 or index < len(pirate_ship):
            if pirate_ship[index] + repair > section_health:
                pirate_ship[index] = section_health
            else:
                pirate_ship[index] += repair
    elif action == 'Status':
        repair_blocks = 0
        for block in pirate_ship:
            if block < (section_health * 0.2):
                repair_blocks += 1
        print(f"{repair_blocks} sections need repair.")
if battle_finished:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f'Warship status: {sum(warship)}')
