houses = list(map(int, input().split('@')))

index_jumps = 0
while True:
    command = input()
    if command == "Love!":
        break
    data = command.split()
    index_jumps += int(data[1])
    if index_jumps >= len(houses) or index_jumps < 0:
        index_jumps = 0
    if houses[index_jumps] - 2 >= 0:
        houses[index_jumps] -= 2
        if houses[index_jumps] == 0:
            print(f"Place {index_jumps} has Valentine's day.")
    elif houses[index_jumps] == 0:
        print(f"Place {index_jumps} already had Valentine's day.")
print(f"Cupid's last position was {index_jumps}.")

is_sucsessful = True
failed_houses = 0
for heart in houses:
    if heart != 0:
        failed_houses += 1
        is_sucsessful = False
if is_sucsessful:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed_houses} places.")
