# we are making empty list
lst = []
# we are making for loop because in the task we are told that we will have 3 inputs
for _ in range(3):
    # we read our data 3 times and with function append we are adding it to the list(lst)
    data = input()
    lst.append(data)
# we change the sides of the first and last data we receive
lst[0], lst[2] = lst[2], lst[0]
print(lst)

# --------------------------------- 01. Strange Zoo ---------------------
# You will receive 3 strings on separate lines, representing the tail, the body, and the head of an animal in that order.\
# Your task is to re-arrange the elements in a list so that the animal looks normal again:
#
# · On the first position is the head;
#
# · On the second position is the body;
#
# · On the last one is the tail.

# Inputs:
# my tail
# my body seems on place
# my head is on the wrong end!
# ------
# tail
# body
# head
# ------
# T
# B
# H
# -----------
# Outputs:
# ['my head is on the wrong end!', 'my body seems on place', 'my tail']
# ['head', 'body', 'tail']
# ['H', 'B', 'T']