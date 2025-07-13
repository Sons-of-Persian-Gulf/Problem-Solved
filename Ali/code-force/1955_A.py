for _ in range(int(input())):
    n, a, b = map(int, input().split())

    cost = b / 2
    if a < cost:
        print(n * a)
    else:
        print((n // 2) * b + (n % 2) * a)