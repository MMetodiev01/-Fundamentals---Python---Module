# def coffee(quantity):
#     return f'{1.50 * quantity:.2f}'
#
#
# def water(quantity):
#     return f'{1 * quantity:.2f}'
#
#
# def coke(quantity):
#     return f'{1.40 * quantity:.2f}'
#
#
# def snacks(quantity):
#     return f'{2 * quantity:.2f}'
#
#
# name_of_product = input()
# number = int(input())
#
# while True:
#
#     if name_of_product == 'coffee':
#         print(f'{coffee(number)}')
#         break
#
#     if name_of_product == 'water':
#         print(f'{water(number)}')
#         break
#
#     if name_of_product == 'coke':
#         print(f'{coke(number)}')
#         break
#
#     if name_of_product == 'snacks':
#         print(f'{snacks(number)}')
#         break

def products_name(name, quantity):
    if name == 'coffee':
        return f'{1.50 * quantity:.2f}'
    elif name == 'water':
        return f'{1 * quantity:.2f}'
    elif name == 'coke':
        return f'{1.40 * quantity:.2f}'
    elif name == 'snacks':
        return f'{2 * quantity:.2f}'


product = input()
number_of_product = int(input())
print(products_name(product, number_of_product))
