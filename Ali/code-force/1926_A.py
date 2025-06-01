t = int(input())


for _ in range(t):
    a = 0
    b = 0
    for i in input():
        if i == "A":
            a += 1
        else:
            b += 1
    print("A" if a > b else "B")