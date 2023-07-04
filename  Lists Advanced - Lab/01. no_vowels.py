text = input()
vow_list = ['a', 'o', 'u', 'e', 'i']
result = [x for x in text if x.lower() not in vow_list]
print(*result, sep='')

# Example 2:
# def vowels(intro):
#     vow_list = ['a', 'o', 'u', 'e', 'i']
#     result = []
#     for letter in intro:
#         if letter not in vow_list:
#             result.append(letter)
#     return ''.join(result)
#
#
# text = input()
# print(vowels(text))

# --------------------------------- 01. No Vowels ---------------------
# Using comprehension, write a program that receives a text and removes all its vowels, case-insensitive.\
# Print the new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i

# Inputs:        Outputs:
# Python         | Pythn
# ILovePython    | LvPythn
