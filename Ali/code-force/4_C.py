n = int(input())

d = dict()

for _ in range(n):
    x = input()
    if x not in d:
        d[x] = 1
        print("OK")
    else:
        print(f"{x}{d[x]}")
        d[x] += 1
