for _ in range(int(input())):
    x1, y1 = map(int, input().split())
    m = -float("inf")
    for _ in range(3):
        x2, y2 = map(int, input().split())

        if abs(x1 - x2) > m:
            m = abs(x1 - x2)
    print(m ** 2)
    