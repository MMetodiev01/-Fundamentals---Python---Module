row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))

column1 = [row1[0], row2[0], row3[0]]
column2 = [row1[1], row2[1], row3[1]]
column3 = [row1[2], row2[2], row3[2]]

diagonal1 = [row1[0], row2[1], row3[2]]
diagonal2 = [row1[2], row2[1], row3[0]]

if row1.count(1) == 3 or row2.count(1) == 3 or row3.count(1) == 3:
    print("First player won")
elif row1.count(2) == 3 or row2.count(2) == 3 or row3.count(2) == 3:
    print("Second player won")
elif column1.count(1) == 3 or column2.count(1) == 3 or column3.count(1) == 3:
    print("First player won")
elif column1.count(2) == 3 or column2.count(2) == 3 or column3.count(2) == 3:
    print("Second player won")
elif diagonal1.count(1) == 3 or diagonal2.count(1) == 3:
    print("First player won")
elif diagonal1.count(2) == 3 or diagonal2.count(2) == 3:
    print("Second player won")
else:
    print("Draw!")
