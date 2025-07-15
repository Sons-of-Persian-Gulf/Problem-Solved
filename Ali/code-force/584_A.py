n, t = map(int, input().split())

a = int("1" + "0" * (n - 1))
b = int("1" + "0" * n) - 1

x = a + (t - (a % t))
if a <= x <= b:
    print(x)
else:
    print(-1)

