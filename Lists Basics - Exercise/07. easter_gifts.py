gifts_list = input().split()
# we make while loop until the condition is True
while True:
    command = input()
    # we make variable command for the commands that we receive
    if command == 'No Money':
        break
    # we make another variable to split the command to know which is a command(order) and which is a gift
    data = command.split()
    order = data[0]
    gift = data[1]
    if order == 'OutOfStock':
        # we ask if the gift is in the gift list
        if gift in gifts_list:
            counter = gifts_list.count(gift)
            # after that we count how many are in the list
            for _ in range(counter):
                # we make for loop in range the counter(counter for how many 'gift' is in the gift list)
                element = gifts_list.index(gift)
                # we make variable element that gives us the 'gift' from the gift list ,so we can swap it with 'None'
                gifts_list[element] = 'None'
                # last we say the exact element from the gift list to be replaced it with 'None'
    elif order == 'Required':
        index_of_gift = int(data[2])
        # we make variable for the index_jumps we receive if the order is 'Required'
        if index_of_gift >= 0 and index_of_gift < len(gifts_list):
            # we ask if the index_jumps is in the exact range of the list because if is not we can replace it
            gifts_list[index_of_gift] = gift
            # then in the gift list on that index_jumps we say 'replace it with the gift'
    elif order == 'JustInCase':
        gifts_list[-1] = gift
# in the end we make for loop to go through the names in the list
for names in gifts_list:
    if names != 'None':
        print(names, end=' ')

# --------------------------------- 07. Easter Gifts ---------------------
# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family.
# First, you are going to receive the gifts you plan on buying on a single line,
# separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {gift}"
# Then you will start receiving commands until you read the "No Money" message.
# There are three possible commands:
# •	"OutOfStock {gift}"
# o	Find the gifts with this name in your collection, if any, and change their values to "None".
# •	"Required {gift} {index_jumps}"
# o	If the index_jumps is valid, replace the gift on the given index_jumps with the given gift.
# •	"JustInCase {gift}"
# o	Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None",
#  separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"
# Input / Constraints
# •	On the 1st line,  you will receive the names of the gifts, separated by a single space.
# •	On the following lines, until the "No Money" command is received, you will be receiving commands.
# •	The input will always be valid.
# Output
# •	Print the gifts in the format described above.

# Inputs:
# Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes
# OutOfStock Eggs
# Required Spoon 2
# JustInCase ChocolateEgg
# No Money

# Sweets Cozonac Clothes Flowers Wine Clothes Eggs Clothes
# Required Paper 8
# OutOfStock Clothes
# Required Chocolate 2
# JustInCase Hat
# OutOfStock Cable
# No Money
# ---------------
# Ouputs:
# StuffedAnimal Spoon Sweets EasterBunny ChocolateEgg
# Sweets Cozonac Chocolate Flowers Wine Eggs Hat
