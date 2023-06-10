names = input().split(', ')
result = sorted(names, key=lambda item: (-len(item), item))
print(result)
# we split the names like is given from the task
# we need to tell the sorted method how we want to sort our objects(names)
# for that we will use key parameter
# we will tell sorted that for each name(item) we want to take the length of the name(item) as the sorting key
# this means that each name will be compared against other names by looking only at their length
