budget_available = int(input())

current_price = input()
while current_price != 'End':

    now_price = int(current_price)

    budget_available -= now_price

    if budget_available < 0:
        print('You went in overdraft!')
        break

    current_price = input()
    if current_price == 'End':
        print('You bought everything needed.')
        break


#
# 100
# 5
# End


# budget_available = int(input())
# while True:
#     price = input()
#
#     if price == "End":
#         print('You bought everything needed.')
#         break
#
#     price = int(price)
#
#     budget_available -= price
#
#     if budget_available < 0:
#         print('You went in overdraft!')
#         break
# 50
# 25
# 20
# 10