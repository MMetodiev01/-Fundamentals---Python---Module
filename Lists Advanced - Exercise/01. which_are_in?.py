first_sequence = input().split(", ")
second_sequence = input().split(", ")
substring = []
for first_word in first_sequence:
    for second_word in second_sequence:
        if first_word in second_word:
            substring.append(first_word)
            break
print(substring)

# --------------------------------- 01. Which Are In? ---------------------
# You will be given two sequences of strings, separated by ", ".
# Print a new list containing only the strings from the first input line,\
# which are substrings of any string in the second input line

# Inputs:
# arp, live, strong
# lively, alive, harp, sharp, armstrong
# ----------
# tarp, mice, bull
# lively, alive, harp, sharp, armstrong

# Outputs:
# ['arp', 'live', 'strong']
# []
