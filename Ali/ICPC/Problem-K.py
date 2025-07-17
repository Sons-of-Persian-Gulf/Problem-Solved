n, k = map(int, input().split())
arr = []
cnt = 0
for _ in range(n):
    if cnt < k:
        arr.append(input())
    else:
        input()
    cnt += 1
arr = sorted(arr)
for i in arr:
    print(i)

