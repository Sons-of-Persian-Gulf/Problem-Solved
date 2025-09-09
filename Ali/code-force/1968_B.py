for _ in range(int(input())):
    n, m = map(int, input().split())
    a = input()
    b = input()
    index = 0
    cnt = 0
    for i in a:
        while True and index < m:
            if i == b[index]:
                cnt += 1
                index += 1
                break
            index += 1
    print(cnt)