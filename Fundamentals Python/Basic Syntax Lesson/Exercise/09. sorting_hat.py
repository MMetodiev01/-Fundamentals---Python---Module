names = input()

while names != "Welcome!":
    if names == "Voldemort":
        print("You must not speak of that name!")
        break
    length = len(names)

    if length < 5:
        print(f"{names} goes to Gryffindor.")
    elif length == 5:
        print(f"{names} goes to Slytherin.")
    elif length == 6:
        print(f"{names} goes to Ravenclaw.")
    else:
        print(f"{names} goes to Hufflepuff.")

    names = input()
    command = names
    if command == "Welcome!":
        print('Welcome to Hogwarts.')
        break


# Option 2 from git

# while True:
#     type_ticket = input()
#     if type_ticket == 'Welcome!':
#         print('Welcome to Hogwarts.')
#         break
#     name = type_ticket
#     if name == 'Voldemort':
#         print("You must not speak of that name!")
#         break
#     elif len(name) < 5:
#         print(f"{name} goes to Gryffindor.")
#     elif len(name) == 5:
#         print(f"{name} goes to Slytherin.")
#     elif len(name) == 6:
#         print(f"{name} goes to Ravenclaw.")
#     else:
#         print(f"{name} goes to Hufflepuff.")