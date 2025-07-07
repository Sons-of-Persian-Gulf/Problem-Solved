a, b = map(int, input().split())

x1 = min(a, b)
a -= x1
b -= x1
print(x1, (a + b) // 2)