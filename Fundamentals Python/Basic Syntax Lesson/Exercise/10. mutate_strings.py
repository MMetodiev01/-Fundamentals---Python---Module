first_string = input()
second_string = input()
last_printed_string = first_string
for character_index in range(len(first_string)):
    left_part = second_string[:character_index + 1]
    right_part = first_string[character_index + 1:]
    current_name = left_part + right_part
    if current_name == last_printed_string:
        continue
    print(current_name)
    last_printed_string = current_name


