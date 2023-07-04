import random


# contains some functionality that helps us generate random numbers
# we make function roll dice with parameter that is equal to 2 if the user don't specify anything it will roll dice two times\
# and it will return us a list of integers
def roll_dice(amount=2) -> list[int]:
    # we must check if the amount is less or equal to zero
    if amount <= 0:
        raise ValueError
    rolls = []
    for i in range(amount):
        random_rolls = random.randint(1, 6)
        # when we go through the loop it will roll dice to a random number from 1 to 6
        rolls.append(random_rolls)
    return rolls


def main():
    while True:
        try:
            user_input = input('How many dice would like to roll? ')
            if user_input.lower() == 'exit':
                print('Thanks for playing!')
                break
            print(*roll_dice(int(user_input)), sep=', ')
        except ValueError:
            print('Please enter valid number!')


if __name__ == '__main__':
    main()

# TASK: Return to user the sum of the dice rolls every time he roll the dice
