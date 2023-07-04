products = {}
while True:
    command = input()
    if command == 'statistics':
        break
    key, value = command.split(": ")
    if key not in products.keys():
        products[key] = 0
    products[key] += int(value)
print(f"Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(product)}")
print(f"Total Quantity: {sum([int(s) for s in products.values()])}")
# print(f"Total Quantity: {sum(list(products.values()))}")
