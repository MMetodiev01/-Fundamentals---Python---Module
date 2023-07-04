# we make function to se if one word is palindrome
def palindrome_filter(word):
    if word == word[::-1]:
        return word


# we split the word with space between them
words = input().split(' ')
palindrome_word = input()
# we make empty list to add the palindrome words into the list
palindrome_list = [data for data in words if palindrome_filter(data)]
# Variant 2:
# palindrome_list = []
# for data in words:
#     if palindrome_filter(data):
#         palindrome_list.append(data)

# after that we count much is the palindrome word is in the palindrome list
count_palindrome = palindrome_list.count(palindrome_word)
print(palindrome_list)
print(f'Found palindrome {count_palindrome} times')

# --------------------------------- 04. Palindrome Strings ---------------------
# On the first line, you will receive words separated by a single space.\
# On the second line, you will receive a palindrome.\
# First, you should print a list containing all the found palindromes in the sequence.\
# Then, you should print the number of occurrences of the given palindrome in the format:\
# "Found palindrome {number} times".


# Inputs:
# wow father mom wow shirt stats
# wow
# ----------
# hey how you doin? lol
# mom
# --------
# Outputs:
# ['wow', 'mom', 'wow', 'stats']
# Found palindrome 2 times

# ['lol']
# Found palindrome 0 times
