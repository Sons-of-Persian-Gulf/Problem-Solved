for _ in range(int(input())):
    n, k = map(int, input().split())
    if k in map(int, input().split()):
        print("YES")
    else:
        print("NO")