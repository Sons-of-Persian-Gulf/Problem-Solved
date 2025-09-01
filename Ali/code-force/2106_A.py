for _ in range(int(input())):
    n = int(input())
    s = input()
    one = 0
    zero = 0
    if s == "1":
        print(0)
    else:
        for i in s:
            if i == "1":
                one += 1
            else:
                zero += 1
        print(((one * n) - one) + zero)