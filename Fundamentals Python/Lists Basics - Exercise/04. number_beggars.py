money = input().split(", ")
money_as_int = []
# we go through every element in money(str) to make them an integer to calculate how much one beggar take
for current_money in money:
    money_as_int.append(int(current_money))

beggars = int(input())
# after that we make an empty list for how much one beggar take 'and' we implement starting point\
# from where to start to take(starting_index)
total_for_beggar = []
starting_index = 0
# we make while loop 'and we say 'while the positions for beggars are smaller than the beggars
while starting_index < beggars:
    # we make variable to be equal to zero because for every new beggar they will have nothing
    sum_for_beggar = 0
    # for the first beggar we start from our implement starting index and finish to length of our money list and with that we know
    # that the beggar will take what he deserves with step how many beggars there are
    for current_beggar in range(starting_index, len(money_as_int), beggars):
        # we sum up what beggar take from 'money as digit list in our variable and after that we append it in our total list
        sum_for_beggar += money_as_int[current_beggar]
    total_for_beggar.append(sum_for_beggar)
    # after the beggar finishes, we sum up our index to start the next beggar from the next position
    starting_index += 1
print(total_for_beggar)
# --------------------------------- 04. Number Beggars ---------------------
# You will receive 2 lines of input.\
# On the first line, you will receive a single string of integers, separated by a comma and a space ", ".\
# On the second line, you will receive a count of beggars.\
# Your job is to print a list with the sum of what each beggar brings home, assuming they all take regular turns, from the first to the last number in the list.
# For example: [1, 2, 3, 4, 5] for 2 beggars will return a result of 9 and 6, as the first one takes [1, 3, 5], the second one collects [2, 4].\
# The same list with 3 beggars would produce a better outcome for the second beggar: 5, 7 and 3, as they will respectively take [1, 4], [2, 5], and [3].\
# Also, note that not all beggars have to take the same amount of "offers", meaning that the length of the list is not necessarily a multiple of number.\
# The list length could be even shorter - i.e., the last beggars will take nothing (0)
# Inputs:
# 1, 2, 3, 4, 5
# 2
# 3, 4, 5, 1, 29, 4
# 6
# 100, 94, 24, 99
# 5
# Outputs:
# [9, 6]
# [3, 4, 5, 1, 29, 4]
# [100, 94, 24, 99, 0]