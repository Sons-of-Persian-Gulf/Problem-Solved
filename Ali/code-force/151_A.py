n, k, l, c, d, p, nl, np = map(int, input().split())

milli_liter = k * l
lime_slice = c * d

x1 = milli_liter // (n * nl)
x2 = lime_slice // n
x3 = p // (n * np)
print(min(x1, x2, x3))