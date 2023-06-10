numbers = input().split(" ")
elements = []

for num in numbers:
    elements.append(abs(float(num)))
print(elements)