for _ in range(int(input())):
    n, k = map(int, input().split())

    max_edges = (n * (n - 1)) // 2
    x = n - 1
    if k < n - 1:
        print(n)
    elif k >= n - 1:
        print(1)