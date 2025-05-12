n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort(key=lambda item: (item[0], item[1]))
flag = False
for i in range(0, n - 1):
    price, quality = arr[i]
    if price < arr[i + 1][0] and quality > arr[i + 1][1]:
        flag = True
        break
print("Happy Alex" if flag else "Poor Alex")