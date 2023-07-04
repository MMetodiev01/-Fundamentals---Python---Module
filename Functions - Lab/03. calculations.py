def calculation(number_a, number_b, type_of_operation):
    if type_of_operation == 'multiply':
        return number_a * number_b
    elif type_of_operation == 'divide':
        return int(number_a / number_b)
    elif type_of_operation == 'add':
        return number_a + number_b
    elif type_of_operation == 'subtract':
        return number_a - number_b


operation = input()
first_number = int(input())
second_number = int(input())
print(calculation(first_number, second_number, operation))
# def intro():
#     return 'Hello! This is simple calculator\nChoose operation: '
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divided(n1, n2):
#     return n1 / n2
#
#
# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# print(intro())
#
# while True:
#     choices = input('1.Multiply\n2.Divided\n3.Add\n4.Subtract\n5.Exit from calculator\nEnter choice: ')
#
#     if choices == '5':
#         print('You exit from calculator')
#         break
#     n1 = int(input('Enter first number: '))
#     n2 = int(input('Enter second number: '))
#
#     if choices == '1':
#         print(f'Result: {multiply(n1, n2)} \number')
#
#     if choices == '2':
#         print(f'Result: {divided(n1, n2)} \number')
#
#     if choices == '3':
#         print(f'Result: {add(n1, n2)} \number')
#
#     if choices == '4':
#         print(f'Result: {subtract(n1, n2)} \number')
