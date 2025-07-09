for _ in range(int(input())):
    a, b, c = map(int, input().split())
    x1 = a - 1
    x2 = abs(b - c) + abs(c - 1)
    if x1 < x2:
        print(1)
    elif x1 > x2:
        print(2)
    else:
        print(3)
