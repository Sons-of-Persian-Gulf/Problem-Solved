n = int(input())
arr = list(map(int, input().split()))

cnt = 0
mn = mx = arr[0]

for i in range(1, n):
    if arr[i] > mx:
        cnt += 1
        mx = arr[i]
    elif arr[i] < mn:
        cnt += 1
        mn = arr[i]

print(cnt)
