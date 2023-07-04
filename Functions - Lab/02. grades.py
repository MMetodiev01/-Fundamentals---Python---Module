# # ------------------------- IMPROVISE ANSWER ----------------- #
# def choice():
#     return 'Enter student grade:'
#
#
# def fail(n):
#     return 'Fail'
#
#
# def poor(n):
#     return 'Poor'
#
#
# def good(n):
#     return 'Good'
#
#
# def very_good(n):
#     return 'Very Good'
#
#
# def excellent(n):
#     return 'Excellent'
#
#
# print(choice())
# number = float(input())
#
# while True:
#
#     if 2.00 <= number <= 2.99:
#         print(f'Result: {fail(number)} \n')
#         break
#
#     if 3.00 <= number <= 3.49:
#         print(f'Result: {poor(number)} \n')
#         break
#
#     if 3.50 <= number <= 4.49:
#         print(f'Result: {good(number)} \n')
#         break
#
#     if 4.50 <= number <= 5.49:
#         print(f'Result: {very_good(number)} \n')
#         break
#
#     if 5.50 <= number <= 6.00:
#         print(f'Result: {excellent(number)} \n')
#         break

def grade(num):
    if 2.00 <= num <= 2.99:
        return 'Fail'
    elif 3.00 <= num <= 3.49:
        return 'Poor'
    elif 3.50 <= num <= 4.49:
        return 'Good'
    elif 4.50 <= num <= 5.49:
        return 'Very Good'
    elif 5.50 <= num <= 6.00:
        return 'Excellent'


number = float(input())
print(grade(number))
