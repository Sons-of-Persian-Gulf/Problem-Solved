for _ in range(int(input())):
    a, b, c, d = map(int ,input().split())
    if b > d or (d - b) < (c - a):
        print(-1)
    else:
        result = 2*(d - b) + (a - c)
        print(result)