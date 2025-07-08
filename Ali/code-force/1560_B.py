for _ in range(int(input())):
    a, b, c = map(int, input().split())

    n = abs(a - b) * 2
    if a > n or b > n or c > n:
        print(-1)
    else:
        x = (c + (n // 2))
        if x == n:
            print(x)
        else:
            print(x % n)
