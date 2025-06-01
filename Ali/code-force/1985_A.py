n = int(input())

for _ in range(n):
    a, b = input().split()
    x1 = b[0] + a[1:]
    x2 = a[0] + b[1:]
    print(x1, x2)