my_list = [1, 2, 3, 4, "b", "a", "g", 2, 2, 2, 2]
my_numbers_list = [1, 2, 3, 4, 2, 2, 2, 2]
my_letters_list = ["k", "a", "c", "m"]

# --------------------------------- APPEND ---------------------------------------
#
# indexes = []
# for index_jumps, element in enumerate(my_numbers_list):
#     if int(element) == 2:                          # for every index_jumps with number 2
#         indexes.append(index_jumps)                      # add indexes in new list
# print(indexes)
# Result
# [1, 4, 5, 6, 7]


# --------------------------------- SORT ---------------------------------------
#
# my_letters_list.sort(reverse=True)    # sort and reverse
# print(my_letters_list)
# print(sorted(my_letters_list))
# Result
# ['m', 'k', 'c', 'a']
# ['a', 'c', 'k', 'm']


# ---------------------------------- POP -----------------------------------------
#
# char = my_list.pop(-5)                # removes specific index_jumps element and returns it
# print(my_list)                        # if only () deletes last element and returns it
# print(char)
# Result
# [1, 2, 3, 4, 'b', 'a', 'g', 2, 2, 2]
# 2


# --------------------------------- REMOVE ----------------------------------------
#
# while 2 in my_list:                   # removes specific element
#     my_list.remove(2)
# print(my_list)
# Result
# [1, 3, 4, 'b', 'a', 'g']
#
# while my_list.count(2) > 1:             # while in list there is only one number 2
#     my_list.remove(2)
# print(my_list)
# Result
# [1, 2, 3, 4, "b", "a", "g", 2]
#
# my_list.remove(2)                       # removes first number 2
# print(my_list)
# Result
# [1, 3, 4, "b", "a", "g", 2, 2, 2, 2]


# ---------------------------------  INSERT ---------------------------------------
#
# my_list.insert(5, "Pesho")            # on index_jumps 5 insert specific string
# print(my_list)
# Result
# [1, 2, 3, 4, 'b', 'Pesho', 'a', 'g', 2, 2, 2, 2]


# ---------------------------------- INDEX -----------------------------------------
#
# number = my_list.index_jumps(2)               # first index_jumps where can find number 2 is index_jumps 1
# print(number)
# Result
# 1
# ---------------------
# list1 = [5, 10, 15, 20, 25, 50, 20]
#
# # get the first occurrence index_jumps
# index_jumps = list1.index_jumps(20)
#
# # update days present at location
# list1[index_jumps] = 200
# print(list1)


# ---------------------------------- COUNT -----------------------------------------
#
# repetition = my_list.count(2)           # how many times there is repeated number 2
# print(repetition)
# Result
# 5


# ---------------------------------- REVERSE -----------------------------------------
#
# my_list.reverse()
# Result
# [2, 2, 2, 2, 'g', 'a', 'b', 4, 3, 2, 1]
#
# print(my_numbers_list[::-1])
# Result
# [2, 2, 2, 2, 'g', 'a', 'b', 4, 3, 2, 1]
#
# print(my_numbers_list[:3])
# Result
# [2, 2, 2, 2]
#
# print(my_numbers_list[3:])
# Result
# [4, 'b', 'a', 'g', 2, 2, 2, 2]
#
# print(my_numbers_list[3:5])
# Result
# [2, 2, 2, 2]


# ---------------------------------- DEL -----------------------------------------
#
# del my_numbers_list[0]                      # delete first index_jumps
# print(my_numbers_list)
# Result
# [2, 3, 4, 2, 2, 2, 2]


# ---------------------------------- COPY -----------------------------------------
#
# my_second_list = my_list.copy()             # because if it is not copy, two lists will
# my_second_list.remove(2)                    # be modified simultaneously
# print(my_list)
# print(my_second_list)


# ---------------------------------- MIN -----------------------------------------
#
# min_number = min(my_numbers_list)
# print(min_number)


# ---------------------------------- MAX -----------------------------------------
#
# max_number = min(my_numbers_list)
# print(max_number)


# --------------------------------- FILTER ----------------------------------------
#
# filtered_numbers = filter(lambda x: x % 2 == 0, my_numbers_list)
# print(list(filtered_numbers))
# Result
# [2, 4, 2, 2, 2, 2]


# --------------------------------- EXTEND ----------------------------------------
#
# my_numbers_list.extend([4, 5])
# Result:
# [1, 2, 3, 4, 2, 2, 2, 2, 4, 5]


# ----------------------------------- CLEAR ----------------------------------------
#
# my_numbers_list.clear()
# Result:
# []


# ----------------------------------- SWAP ----------------------------------------
#
# lst = [1, 2, 3, 4]
# print("list before swapping:", lst)
#
# lst[1], lst[2] = lst[2], lst[1]
# print("list after swapping:", lst)


# ----------------------------------- SET ----------------------------------------
#
# numbers = [1, 2, 2, 2, 3, 4, 5, 5, 6]
# unique_numbers = list(set(numbers))
# Result:
# [1, 2, 3, 4, 5, 6]
