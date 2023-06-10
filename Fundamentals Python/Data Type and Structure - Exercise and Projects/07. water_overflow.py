number_of_liters = int(input())
capacity = 255
water_count = 0
for current_liters in range(number_of_liters):
    liters_of_water = int(input())
    capacity -= liters_of_water
    if capacity - liters_of_water < 0:
        print("Insufficient capacity!")
        continue
    water_count += liters_of_water
print(water_count)
