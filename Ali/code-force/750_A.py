time_have = 60 * 4
n, k = map(int, input().split())
time_have -= k
cnt = 0
for i in range(1, n + 1):
    t = i * 5  # Time needed to solve ith problem
    if time_have >= t:
        time_have -= t
        cnt += 1
    else:
        break

print(cnt)