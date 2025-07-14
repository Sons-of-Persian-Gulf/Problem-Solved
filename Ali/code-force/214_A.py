n, m = map(int, input().split())

cnt = 0

for i in range(0, int(n ** .5) + 1):
    b = i ** 2 - n
    if i + b ** 2 == m:
        cnt += 1
print(cnt)