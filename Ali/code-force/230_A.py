s, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda item: item[0])
# print(arr)
flag = True
for x, y in arr:
    if s > x:
        s += y
    else:
        flag = False
        break
print("YES" if flag else "NO")