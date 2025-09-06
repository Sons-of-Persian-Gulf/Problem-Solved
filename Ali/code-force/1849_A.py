for _ in range(int(input())):
    b, c, h = map(int, input().split())

    if b > c + h:
        print((c + h) * 2 + 1)
    else:
        print((b * 2) - 1)
