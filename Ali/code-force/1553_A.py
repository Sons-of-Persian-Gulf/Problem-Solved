for _ in range(int(input())):
    x = int(input())
    c = 1 if x % 10 == 9 else 0
    print((x // 10) + c)