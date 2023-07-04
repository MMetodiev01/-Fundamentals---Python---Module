food_in_grams = float(input()) * 1000
hay_in_grams = float(input()) * 1000
cover_in_grams = float(input()) * 1000
weight_in_grams = float(input()) * 1000

is_enough = True
count_days = 0
for days in range(1, 31):
    count_days += 1
    food_in_grams -= 300
    if days % 2 == 0:
        needed_hay = food_in_grams * 0.05
        hay_in_grams -= needed_hay
    if days % 3 == 0:
        cover_need = weight_in_grams / 3
        cover_in_grams -= cover_need

    if food_in_grams <= 0 or hay_in_grams <= 0 or cover_in_grams <= 0:
        is_enough = False
        break
food_kg = food_in_grams / 1000
hay_kg = hay_in_grams / 1000
cover_kg = cover_in_grams / 1000
if is_enough:
    print(
        f"Everything is fine! Puppy is happy! Food: {food_kg:.2f}, Hay: {hay_kg:.2f}, Cover: {cover_kg:.2f}.")
else:
    print("Merry must go to the pet store!")
