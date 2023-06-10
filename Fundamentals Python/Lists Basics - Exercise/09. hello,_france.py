items = input().split("|")
budget = float(input())

ticket = 150
sell_items = []

for elements in items:
    data = elements.split("->")
    type_item = data[0]
    value = float(data[1])
    if type_item == "Clothes" and value <= 50:
        if budget - value >= 0:
            budget -= value
            selling_price = value * 1.40
            sell_items.append(selling_price)
    elif type_item == "Shoes" and value <= 35:
        if budget - value >= 0:
            budget -= value
            selling_price = value * 1.40
            sell_items.append(selling_price)
    elif type_item == "Accessories" and value <= 20.50:
        if budget - value >= 0:
            budget -= value
            selling_price = value * 1.40
            sell_items.append(selling_price)
profit_of_sells = sum(sell_items) - (sum(sell_items) / 1.40)
for money in sell_items:
    print(*[f'{money:.2f}'], end=" ")
print()
print(f'Profit: {profit_of_sells:.2f}')
total_money = sum(sell_items) + budget
if total_money >= ticket:
    print('Hello, France!')
else:
    print('Not enough money.')

# Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
# 120