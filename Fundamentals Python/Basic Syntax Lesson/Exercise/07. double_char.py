command = input()

while command != "End":
    if command != "SoftUni":
        current_string = ''
        for letter in command:
            current_string += letter * 2
        print(current_string)
    command = input()