for _ in range(int(input())):
    d = dict()
    n = int(input())
    s = input()
    cnt = 0
    for i in range(1, n):
        x = s[i - 1: i + 1]
        if x in d:
            continue
        else:
            d[x] = 1
            cnt += 1
    print(cnt)
    # print("------------------")
