n, k = map(int, input().split())
cnt = 0
arr = list(map(int, input().split()))
for i in (arr):
    if i >= arr[k - 1] and i > 0:
        cnt += 1
print(cnt)