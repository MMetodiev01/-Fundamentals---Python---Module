deck_of_card = input().split()
number_of_shuffle = int(input())
# we make for loop to go through the number of shuffle
for shuffle in range(number_of_shuffle):
    final_shuffle = []
    # we make an empty list to add the shuffled cards
    middle_of_the_deck = len(deck_of_card) // 2
    # we slice the deck in two parts ( with typing the len of the deck and integer division(//) by 2)
    left_part = deck_of_card[:middle_of_the_deck]
    # we make left part of the cards(starts from zero to middle of the deck) and right side
    right_part = deck_of_card[middle_of_the_deck::]
    # we make for loop in range the len of the side(to go through what is in that side) \
    # for one of the sides and append cards from each side in the list
    for card_index in range(len(left_part)):
        final_shuffle.append(left_part[card_index])
        final_shuffle.append(right_part[card_index])
    # last we say that the first deck is equal to the last shuffled deck to start the next shuffle with the last deck
    deck_of_card = final_shuffle
print(deck_of_card)

# --------------------------------- 05. Faro Shuffle ---------------------
# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half.
# Then the cards in the two halves are perfectly interleaved,
# such that the original bottom card is still on the bottom and the original top card is still on top.
#
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once,
# gives ['ace', 'four', 'two', 'five', 'three', 'six']
#
# Write a program that receives a single string (cards separated by space)
# and on the second line receives a count of faro shuffles that should be made. Print the state of the deck after the shuffle.
#
# Note: The length of the deck of cards will always be an even number.
# one two three four
# Inputs:
# one two three four
# 3
# a b c d e f g h
# 5
# -----------
# Outputs:
# ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h'
# ['one', 'three', 'two', 'four']
