n = int(input())
arr = list(map(int, input().split()))
best = 0
cnt = 1

for i in range(n - 1):
    if arr[i + 1] >= arr[i]:
        cnt += 1
    else:
        if cnt > best:
            best = cnt
        cnt = 1

print(max(cnt, best))

