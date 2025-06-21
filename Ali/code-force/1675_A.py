for _ in range(int(input())):
    a, b, c, x, y = map(int, input().split())
    x -= min(a, x)
    y -= min(b, y)
    print("YES" if x + y <= c else "NO")