arr = sorted(list(map(int, input().split())))

x1 = arr[0]
x2 = arr[1]
x3 = arr[2]
x4 = arr[3]

a = x1 + x2 - x4
b = x1 + x3 - x4
c = x2 + x3 - x4
print(a, b, c)
