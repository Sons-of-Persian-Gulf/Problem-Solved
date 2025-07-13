n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
e = 0
for i in range(m):
    if arr[i] < 0:
        e +=  -arr[i]

print(e)