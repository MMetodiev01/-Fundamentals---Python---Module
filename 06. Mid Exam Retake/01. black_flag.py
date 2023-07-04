days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = int(input())

total = 0
for days in range(1, days_of_plunder + 1):
    if days % 3 == 0:
        total += daily_plunder * 1.50
    else:
        total += daily_plunder
    if days % 5 == 0:
        total *= 0.7
if total >= expected_plunder:
    print(f"Ahoy! {total:.2f} plunder gained.")
else:
    diff = total / expected_plunder * 100
    print(f"Collected only {diff:.2f}% of the plunder.")
