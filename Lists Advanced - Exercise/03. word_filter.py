text = input().split(" ")
words = [word for word in text if len(word) % 2 == 0]
print('\n'.join(words))

# --------------------------------- 03. Word Filter ---------------------
# Using comprehension, write a program that receives some text, separated by space,\
# and take only those words whose length is even. Print each word on a new line

# Inputs:
# kiwi orange banana apple
# pizza cake pasta chips

# Outputs:
# kiwi
# orange
# banana
# ---
# cake
