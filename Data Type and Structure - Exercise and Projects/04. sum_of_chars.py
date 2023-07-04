number_of_lines = int(input())
total = 0
for letters in range(number_of_lines):
    letter = ord(input())
    total += letter
print(f"The sum equals: {total}")

