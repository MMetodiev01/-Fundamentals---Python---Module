# we read the numbers from input
numbers = input().split(", ")
# then we make empty list to add numbers in there to integers
elements = []
# after that we make counter for zeros
counter_0 = 0
for num in numbers:
    elements.append(int(num))
# then we tell 'while we have zeros in the list add to counter +1 and remove the zeros'
while 0 in elements:
    counter_0 += 1
    elements.remove(0)
# in the end we say 'while counter_0 is bigger then zero remove from counter -1 and add zero(and the zero will be the last num.)
while counter_0 > 0:
    counter_0 -= 1
    elements.append(0)
print(elements)


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



