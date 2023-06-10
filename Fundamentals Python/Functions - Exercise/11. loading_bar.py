def status(number):
    if number == 100:
        return f"{number}% Complete!\n[{'%' * (number // 10)}]"
    return f"{number}% [{'%' * (number // 10)}{'.' * (10 - number // 10)}]\nStill loading..."


single_number = int(input())
print(status(single_number))

# --------------------------------- 11. Loading Bar ---------------------
# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder (0, 10, 20, 30...).\
# Your task is to create a function that returns a loading bar depending on the number you have received in the input.\
# Print the result on the console. For more clarification, see the examples below.

# Inputs:
# 30
# 50
# 100

# Outputs:
# 30% [%%%.......]
# Still loading...
# ----------
# 50% [%%%%%.....]
# Still loading...
# ----------
# 100% Complete!
# [%%%%%%%%%%]
