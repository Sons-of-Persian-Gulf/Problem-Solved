for _ in range(int(input())):
    n, m = map(int, input().split())
    x = input()
    s = input()
    cnt = 0
    flag = False
    for i in range(6):
        if s in x:
            flag = True
            break
        x *= 2
        cnt += 1

        
    print(cnt if flag else -1)

