t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)