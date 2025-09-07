for _ in range(int(input())):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    product = 1
    for x in b:
        product *= x

    if 2023 % product != 0:
        print("NO")
    else:
        print("YES")
        missing = [1] * (k - 1) + [2023 // product]
        print(*missing)
