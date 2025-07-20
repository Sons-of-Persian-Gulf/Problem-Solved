for _ in range(int(input())):
    n = int(input())
    a = (2 ** n) + (2 ** (n // 2)) - 2
    b = 2 ** (n + 1) - a - 2
    print(abs(a - b))