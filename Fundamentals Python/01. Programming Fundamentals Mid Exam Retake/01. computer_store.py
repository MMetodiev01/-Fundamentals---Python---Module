data = input()
no_tax_price = 0
type_customer_list = ["special", "regular"]
is_special = False
while True:
    if data == type_customer_list[0]:
        is_special = True
        break
    elif data == type_customer_list[1]:
        break

    cur_price = float(data)
    if cur_price >= 0:
        no_tax_price += cur_price
    else:
        print("Invalid price!")
    data = input()
if no_tax_price == 0:
    print("Invalid order!")
else:
    total_price = no_tax_price * 1.2
    taxes = total_price - no_tax_price
    if is_special:
        total_price *= 0.9
        print("Congratulations you've just bought a new computer!")
        print(f'Price without taxes: {no_tax_price:.2f}$')
        print(f'Taxes: {taxes:.2f}$')
        print(f"-----------\nTotal price: {total_price:.2f}$")
    else:
        print("Congratulations you've just bought a new computer!")
        print(f'Price without taxes: {no_tax_price:.2f}$')
        print(f'Taxes: {taxes:.2f}$')
        print(f"-----------\nTotal price: {total_price:.2f}$")

# -------------------------------------------------------------------------
