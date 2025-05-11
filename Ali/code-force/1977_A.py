for _ in range(int(input())):
    n, m = map(int, input().split())

    if n >= m and n % 2 == m % 2:
        print("YES")
    else:
        print("NO")