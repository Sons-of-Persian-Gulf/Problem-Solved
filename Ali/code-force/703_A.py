mishka = 0
chris = 0

for _ in range(int(input())):
    x, y = map(int, input().split())

    if x > y:
        mishka += 1
    elif x < y:
        chris += 1


if mishka > chris:
    print("Mishka")
elif mishka < chris:
    print("Chris")
else:
    print("Friendship is magic!^^")
