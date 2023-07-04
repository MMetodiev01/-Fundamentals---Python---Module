people = int(input())
lift = list(map(int, input().split()))

for index, seat in enumerate(lift):
    if seat < 4:
        available = 4 - seat
        if people - available >= 0:
            people -= available
            lift[index] = available
        else:
            lift[index] = people
            people -= people

is_full = True
for x in range(len(lift)):
    if lift[x] < 4:
        is_full = False

if is_full and people == 0:
    print(' '.join(lift))
elif people == 0:
    print('The lift has empty spots!')
    print(*lift)
else:
    print(f"There isn't enough space! {people} people in a queue!")
    print(*lift)
