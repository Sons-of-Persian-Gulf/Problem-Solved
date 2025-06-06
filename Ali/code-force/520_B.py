n, m = map(int, input().split())

if m <= n:
    print(n - m)
else:
    cnt = 0
    while m > n:
        if m % 2 == 0:
            m //= 2
        else:
            m += 1
        cnt += 1
    cnt += n - m
    print(cnt)
