n = int(input())
a = 0
for i in input():
    if i == "A":
        a += 1

b = n - a
if a > b:
    print("Anton")
elif b > a:
    print("Danik")
else:
    print("Friendship")