for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in arr:
        if i % 2 == 0:
            cnt += 1
    print("YES" if cnt == n else "NO")