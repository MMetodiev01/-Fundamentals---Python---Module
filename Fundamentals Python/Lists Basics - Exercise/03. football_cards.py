# we make the two teams
team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
# we read the players that receive a red card with single space between them
players = input().split()
# we make boolean variable for when one of the teams is left with 7 players or below and referee stop the game
game_was_terminated = False
# after that we need to go through every player and see if it is in team_a or team_b
for player in players:
    # we ask if the player is in the one of the teams if it is remove(.remove) the player (the player is sent off the game)
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
# we have condition that if one of the teams are left with 7 or below players the referee must stop the game,how can we find out\
# how much players are left in the teams without counter, we can check the LENGTH(len) of the teams
    if len(team_a) < 7 or len(team_b) < 7:
        game_was_terminated = True
# the referee stops the game
        break
# after the break the game is stopped
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
# we have to see if the game is stopped and print the corresponding message
if game_was_terminated:
    print("Game was terminated")

# --------------------------------- 03. Football Cards ---------------------
# Most football fans love it for the goals and excitement.\
# Well, this problem does not.\
# You are up to handle the referee's little notebook and count the players who were sent off for fouls and misbehavior.\
# The rules: Two teams, named "A" and "B" have 11 players each.\
# The players on each team are numbered from 1 to 11.\
# Any player may be sent off the field by being given a red card.\
# If one of the teams has less than 7 players remaining, the referee stops the game immediately, and the team with less than 7 players loses.
# The card is a string with the team's letter ("A" or "B") followed by a single dash and the player's number.\
# e.g., the card "B-7" means player #7 from team B received a card.
# The task: You will be given a sequence of cards (could be empty), separated by a single space.\
# You should print the count of remaining players on each team at the end of the game in the format:\
# "Team A - {players_count}; Team B - {players_count}". If the referee terminated the game, print an additional line:\
# "Game was terminated".
# Note for the random tests: If a player who has already been sent off receives another card - ignore it.

# Inputs:
# A-1 A-5 A-10 B-2
# A-1 A-5 A-10 B-2 A-10 A-7 A-3
# -----
# Outputs:
# Team A - 8; Team B - 10
# Team A - 6; Team B - 10 Game was terminated


