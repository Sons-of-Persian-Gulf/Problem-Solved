for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    a = 0
    b = 0
    for i in arr:
        if i % 2 == 0:
            a += i
        else:
            b += i
    print("YES" if a > b else "NO")