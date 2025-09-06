for _ in range(int(input())):
    x = list(input())
    # cnt = abs(int(x[0]) - 1) + 1
    # for i in range(1, 4):
    #     cnt += abs(int(x[i - 1]) - int(x[i])) + 1
    # print(cnt)
    cnt = 0
    cur = 1
    for i in x:
        if i == cur:
            cnt += 1
        elif i == "0":
            cnt += abs(10 - cur) + 1
            cur = 10
        else:
            cnt += abs(int(i) - cur) + 1
            cur = int(i)
    print(cnt)
