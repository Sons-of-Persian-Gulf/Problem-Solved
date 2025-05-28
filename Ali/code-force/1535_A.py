for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    x = min(c, d)
    y = min(a, b)
    if (x > a and x > b) or (y > c and y > d):
        print("NO")
    else:
        print("YES")