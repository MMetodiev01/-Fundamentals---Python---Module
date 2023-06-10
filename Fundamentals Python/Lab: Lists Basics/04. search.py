
number_of_sentence = int(input())
word = input()
# after that we are making two lists: 1 for all sentence and other for sentence with the specific word
lst = []
lst_with_word = []

# we are making for loop to go through all sentence
for _ in range(number_of_sentence):
    data = input()
    lst.append(data)
    # after we read our sentence and add them(.apppend) to the list for all sentence we split the sentence\
    # into words and with the operator 'in' we ask (with if statement) if the word is in this sentence
    data.split()
    # if the word is in this sentence add the sentence to the list with word
    if word in data:
       lst_with_word.append(data)
print(lst)
print(lst_with_word)
# --------------------------------- 04. Search ---------------------
# On the first line, you will receive a number number. On the second line, you will receive a word. \
# On the following number lines, you will be given some strings. You should add them to a list and print them. \
# After that, you should filter out only the strings that include the given word and print that list too.
# Inputs:
# 3
# SoftUni
# I study at SoftUni
# I walk to work
# I learn Python at SoftUni
# ----------
# 4
# tomatoes
# I love tomatoes
# I can eat tomatoes forever
# I don't like apples
# Yesterday I ate two tomatoes
# --------
# Outputs:
# ["I study at SoftUni", "I walk to work", "I learn Python at SoftUni"]
# ["I study at SoftUni", "I learn Python at SoftUni"]
# ---------
# ["I love tomatoes", "I can eat tomatoes forever", "I don't like apples", "Yesterday I ate two tomatoes"]
# ["I love tomatoes", "I can eat tomatoes forever", "Yesterday I ate two tomatoes"]