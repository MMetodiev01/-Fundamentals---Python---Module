def rounding(elements):
    rounded_nums = []
    for item in elements:
        current_item = round(float(item))
        rounded_nums.append(current_item)
    return rounded_nums


numbers = input().split(" ")
print(rounding(numbers))
