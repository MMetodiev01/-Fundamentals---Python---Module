def characters(first, second):
    # we make an empty list to add our characters
    char_list = []
    # we make for loop in range the two elements we receive, and we have to make them to numbers to go through
    for item in range(ord(first) + 1, ord(second)):
        # after that we add them to our list and convert them to characters while we are adding it
        char_list.append(chr(item))
    return char_list


first_elements = input()
second_elements = input()
# we make variable to secure our result from the function
final_result = characters(first_elements, second_elements)
print(' '.join(final_result))
# print(*final_result)

# --------------------------------- 03. Characters in Range ---------------------
# Write a function that receives two characters/
# and returns a single string with all the characters in between them (according to the ASCII code),/
# separated by a single space. Print the result on the console.

# Inputs:
# a
# d
# ----
# #
# :
# -----
# #
# C
# -----
# Outputs:
# b c
# $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9
# $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B
