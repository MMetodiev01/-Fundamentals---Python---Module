key = int(input())
number_of_lines = int(input())
message = ""
for i in range(number_of_lines):
    current_symbol = ord(input())
    new_message = current_symbol + key
    message += chr(new_message)
print(message)