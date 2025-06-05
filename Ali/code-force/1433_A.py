for _ in range(int(input())):
    n = input()
    i = 1
    j = "1"
    cnt = 0
    while True:
        c = j * i
        cnt += len(c)
        if c == n:
            break
        i += 1
        if i == 5:
            i = 1
            j = str(int(j) + 1)
    print(cnt)