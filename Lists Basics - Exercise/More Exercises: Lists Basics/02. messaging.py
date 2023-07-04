numbers = input().split()
sequence = [symbol for symbol in input()]
hidden = []
for num in numbers:
    index = []
    for digit in num:
        index.append(int(digit))
    result = sum(index)
    if result >= len(sequence):
        result -= len(sequence)
    letter = sequence.pop(result)
    hidden.append(letter)
print(''.join(hidden))

#
# numbers = input().split()
# message = [symbol for symbol in input()]
# hidden_message = []
# for number in numbers:
#     index_jumps = sum([int(digit) for digit in number])
#     if index_jumps >= len(message):
#         index_jumps -= len(message)
#     letter = message.pop(index_jumps)
#     hidden_message.append(letter)
