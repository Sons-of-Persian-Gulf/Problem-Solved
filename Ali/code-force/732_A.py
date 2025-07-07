k, r = map(int, input().split())
i = 1
while True:
    if (k * i) % 10 == 0 or (k * i) % 10 == r:
        print(i)
        break
    i += 1

