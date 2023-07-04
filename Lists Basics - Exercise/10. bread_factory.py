action = input().split("|")
initial_energy = 100
initial_coins = 100

is_closed = False

for data in action:
    command = data.split("-")
    event = command[0]
    price = int(command[1])
    if event == "rest":
        energy = initial_energy
        initial_energy += price
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")
    elif event == "order":
        if initial_energy - 30 >= 0:
            initial_energy -= 30
            initial_coins += price
            print(f'You earned {price} coins.')
        else:
            initial_energy += 50
            print(f"You had to rest!")
    else:
        if initial_coins - price >= 0:
            initial_coins -= price
            print(f"You bought {event}.")
        else:
            is_closed = True
            print(f"Closed! Cannot afford {event}.")
            break
if not is_closed:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")

# rest-2|order-10|eggs-100|rest-10
# order-10|order-10|order-10|flour-100|order-100|oven-100|order-1000
