number = list(map(int, input().split(", ")))

for x in number:
    counter = number.count(0)
    for _ in range(counter):
        number.remove(0)
        number.append(0)
    break
print(number)

# --------------------------------- 01. Zeros to Back ---------------------
# Write a program that receives a single string (integers separated by a comma and space ", "),\
# finds all the zeros, and moves them to the back without messing up the other elements.\
# Print the resulting integer list.

# Inputs:
# 1, 0, 1, 2, 0, 1, 3
# 0, 5, 0, 4, 0, 0, 5
# ----------------
# Outputs:
# [1, 1, 2, 1, 3, 0, 0]
# [5, 4, 5, 0, 0, 0, 0]
