for _ in range(int(input())):
    n = int(input())
    s = input()
    d = - float("inf")
    for i in s:
        x = ord(i)
        if x > d:
            d = x
    print(d - 96)
