def f(a, b, c, x):
    return abs(x - a) + abs(x - b) + abs(x - c)
for _ in range(int(input())):
    n = int()
    a, b, c = map(int, input().split())
    print(min(f(a, b, c, a), f(a, b, c, b), f(a, b, c, c)))

    