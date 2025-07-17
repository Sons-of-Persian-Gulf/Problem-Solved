n, s, m, l = map(int, input().split())

best = float("inf")

for i in range(20):
    for j in range(20):
        for c in range(20):
            if i * 6 + j * 8 + c * 12 >= n:
                current =  i * s + m * j + c * l
                if current < best:
                    best = current

print(best)