def valid_password(password):
    # we make boolean variable to see if the password is valid or not
    is_valid = True
    # we make if statements for the conditions that are shown on the task and change the boolean every time to False
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    # .isalnum() is a function that checks if there are letter or number in the password
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    # for the last condition we make counter to check how much digits are in the password
    digit_counter = 0
    for character in password:
        if character.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    return is_valid


login_password = input()
# we make variable that are equal to the function with False conditions and if the boolean variable stays True\
# we make if statement for when is True to print that the 'Password is valid'
password_is_valid = valid_password(login_password)
if password_is_valid:
    print("Password is valid")

# Example 2:
# def valid_password(password):
#     valid_list = []
#     if len(password) < 6 or len(password) > 10:
#         valid_list.append("Password must be between 6 and 10 characters")
#     if not password.isalnum():
#         valid_list.append("Password must consist only of letters and digits")
#     digit_counter = 0
#     for digit in password:
#         if digit.isdigit():
#             digit_counter += 1
#     if digit_counter < 2:
#         valid_list.append("Password must have at least 2 digits")
#     return valid_list
#
#
# login_password = input()
# password_is_valid = valid_password(login_password)
# if len(password_is_valid) == 0:
#     print("Password is valid")
# else:
#     print('\n'.join(valid_password(login_password)))

# --------------------------------- 09. Password Validator ---------------------
# Write a function that checks if a given password is valid. Password validations are:
#
# · It should be 6 - 10 (inclusive) characters long
#
# · It should consist only of letters and digits
#
# · It should have at least 2 digits
#
# If a password is valid, print "Password is valid".
#
# Otherwise, for every unfulfilled rule, print a message:
#
# · "Password must be between 6 and 10 characters"
#
# · "Password must consist only of letters and digits"
#
# · "Password must have at least 2 digits"


# Inputs:
# logIn                     # Password must be between 6 and 10 characters
# Password must have at least 2 digits
# ---------------
# MyPass123                 # Password is valid
# ---------------
# Pa$s$s                    # Password must consist only of letters and digits
# Password must have at least 2 digits
