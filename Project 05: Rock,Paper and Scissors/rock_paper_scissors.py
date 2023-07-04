from random import choice

rps_choices = ['rock', 'paper', 'scissors']


def player_choice():
    print('Select 1 for rock, 2 for paper and 3 for scissors.')

    global player_choice_input

    player_choice_input = int(input('> '))

    if player_choice_input == 1:
        player_choice_input = 'rock'
    elif player_choice_input == 2:
        player_choice_input = 'paper'
    elif player_choice_input == 3:
        player_choice_input = 'scissors'
    return f"You played -- {player_choice_input.upper()} --"


def comp_choice():
    global comp_move

    comp_move = choice(rps_choices)
    return f"Computer played -- {comp_move.upper()} --"


def winLose():
    print()
    rounds_count_comp = 0
    rounds_count_player = 0
    while True:
        if player_choice_input == 'rock' and comp_move == 'paper':
            rounds_count_comp += 1
            return 'COMPUTER WINS THIS ROUND!'
        if player_choice_input == 'scissors' and comp_move == 'rock':
            rounds_count_comp += 1
            return 'COMPUTER WINS THIS ROUND!'
        if player_choice_input == 'paper' and comp_move == 'scissors':
            rounds_count_comp += 1
            return 'COMPUTER WINS THIS ROUND!'
        if player_choice_input == 'rock' and comp_move == 'scissors':
            rounds_count_player += 1
            return 'YOU WIN THIS ROUND!'
        if player_choice_input == 'paper' and comp_move == 'rock':
            rounds_count_player += 1
            return 'YOU WIN THIS ROUND!'
        if player_choice_input == 'scissors' and comp_move == 'paper':
            rounds_count_player += 1
            return 'YOU WIN THIS ROUND!'
        if player_choice_input == comp_move:
            return "THIS ROUND IS DRAW!"


print(player_choice())
print(comp_choice())
print(winLose())
print
