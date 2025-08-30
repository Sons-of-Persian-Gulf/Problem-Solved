n = int(input())
arr = sorted(list(map(int, input().split())))
cnt = 0
for i in range(n // 2):
    cnt += arr[(i * 2) + 1] - arr[i * 2]
print(cnt)
