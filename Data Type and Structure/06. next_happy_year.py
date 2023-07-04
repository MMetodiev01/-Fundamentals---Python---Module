year = int(input())
happy_year = False

while not happy_year:
    year += 1
    filter_years = set()
    for digit in range(len(str(year))):
        filter_years.add(str(year)[digit])

    happy_year = len(filter_years) == len(str(year))

print(year)
