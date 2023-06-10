budget = float(input())
one_kg_flour_price = float(input())
eggs_price = one_kg_flour_price * 0.75
price_liters_milk = one_kg_flour_price * 1.25 / 4
bread_price = one_kg_flour_price + eggs_price + price_liters_milk
colored_eggs_count = 0
breads_count = 0
while budget >= bread_price:
    budget -= bread_price
    breads_count += 1
    colored_eggs_count += 3
    if breads_count % 3 == 0:
        colored_eggs_count -= breads_count - 2
print(f'You made {breads_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.')