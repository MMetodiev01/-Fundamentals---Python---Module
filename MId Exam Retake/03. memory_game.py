numbers = input().split()

moves = 0

while True:
    command = input()
    if command == 'end':
        print("Sorry you lose :(")
        print(*numbers)
        break
    if len(numbers) < 1:
        print(f"You have won in {moves} turns!")
        break
    data = command.split()
    moves += 1
    index_1 = int(data[0])
    index_2 = int(data[1])
    middle = int(len(numbers) / 2)
    if index_1 == index_2 or index_1 < 0 or index_1 >= len(numbers) or \
            index_2 < 0 or index_2 >= len(numbers):
        print("Invalid input! Adding additional elements to the board")
        numbers.insert(middle, f'-{moves}a')
        numbers.insert(middle, f'-{moves}a')
    elif numbers[index_1] == numbers[index_2]:
        element = numbers[index_1]
        print(f"Congrats! You have found matching elements - {element}!")
        numbers.remove(element)
        numbers.remove(element)
    else:
        print('Try again!')
