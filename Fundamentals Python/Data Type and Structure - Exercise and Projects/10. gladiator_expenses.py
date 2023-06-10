lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_helmet = lost_fights // 2
total_sword = lost_fights // 3
total_shield = lost_fights // 6
total_armor = total_shield // 2
expenses = helmet_price * total_helmet + \
    sword_price * total_sword + \
    shield_price * total_shield + \
    armor_price * total_armor
print(f"Gladiator expenses: {expenses:.2f} aureus")


# 23
# 12.50
# 21.50
# 40
# 200