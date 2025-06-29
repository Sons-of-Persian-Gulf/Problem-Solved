n = int(input())

n += 1
while True:
    s = set(str(n))
    if len(s) == 4:
        print(n)
        break
    n = int(n) + 1



