energy = int(input())
initial_energy = energy

is_energy = False
battles = 0
while True:
    command = input()
    if command == "End of battle":
        break
    data = int(command)
    if initial_energy - data >= 0:
        battles += 1
        initial_energy -= data
        if battles % 3 == 0:
            initial_energy += battles
    elif initial_energy - data < 0:
        is_energy = True
        break
if is_energy:
    print(f"Not enough energy! Game ends with {battles} won battles and {initial_energy} energy")
else:
    print(f"Won battles: {battles}. Energy left: {initial_energy}")
