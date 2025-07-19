for _ in range(int(input())):
    n, m, k = map(int, input().split())
    l_pocket = list(map(int, input().split()))
    r_pocket = list(map(int, input().split()))
    cnt = 0
    for i in l_pocket:
        for j in r_pocket:
            if k >= i + j:
                cnt += 1
    print(cnt)
