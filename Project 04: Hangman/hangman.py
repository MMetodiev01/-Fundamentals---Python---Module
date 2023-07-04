from random import choice


def run_game():
    # choice picks random element from the list and return it to word variable
    word = choice(['elephant', 'sunshine', 'bicycle', 'pizza', 'thunder', 'butterfly'])

    username = input('What is your name? >> ')
    print(f'Welcome to Hangman game, {username}!')

    # Setup
    guessed = ''
    tries = int(3)

    while tries > 0:
        blanks = int(0)

        print('Word: ', end='')
        for char in word:
            if char is guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1
        print()

        if blanks == 0:
            print('You got it!')
            break

        guess = input('Enter a letter: ')
        count_guess = 1
        if guess in guessed:
            print(f'You already used: {guess}. Please try with another letter!')
            continue

        if guess == word:
            print(f'You got it from {tries} trie!\n')
            break
        elif len(guess) > count_guess:
            print('Enter one letter please!')
            continue

        guessed += guess
        if guess not in word:
            tries -= 1
            print(f'Sorry that is wrong...({tries} tries remaining)')

            if tries == 0:
                print('No more tries remaining...You lose.')
                break


if __name__ == '__main__':
    run_game()
