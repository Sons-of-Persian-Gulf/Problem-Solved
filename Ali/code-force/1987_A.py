for _ in range(int(input())):
    n, k = map(int, input().split())
    if n == 1:
        print(1)
    else:
        print(1 + (n - 1) * k)