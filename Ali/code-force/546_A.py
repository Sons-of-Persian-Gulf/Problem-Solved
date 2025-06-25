k, n, w = map(int, input().split())

price = int((w / 2) * (2 * k + ((w - 1) * k)))
if n >= price:
    print(0)
else:
    print(abs(n - price))
