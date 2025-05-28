for _ in range(int(input())):
    n = int(input())
    s = input()
    a = 0
    cnt = 0
    for i in s:
        if i == "(":
            a += 1
        else:
            if a >= 1:
                a -= 1
            else:
                cnt += 1

    print(cnt)