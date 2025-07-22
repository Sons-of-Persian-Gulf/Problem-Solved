for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(1, n):
        # for j in range(1, n - j):
        #     if i + j
        if 1 <= n - i <= n:
            cnt += 1
    print(cnt)