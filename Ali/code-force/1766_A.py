for _ in range(int(input())):
    n = input()
    cnt = (len(str(n)) - 1) * 9 + int(n[0])
    print(cnt)