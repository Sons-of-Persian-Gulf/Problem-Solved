d1, d2, d3 = map(int, input().split())
x1 = (d1 + d3) * 2
x2 = (d2 + d3) * 2
x3 = d1 + d2 + d3
x4 = (d1 + d2) * 2
print(min(x1, x2, x3, x4))

