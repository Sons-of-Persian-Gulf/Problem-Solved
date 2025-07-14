for _ in range(int(input())):
    n = int(input())
    best = -float("inf")
    index = 1
    for i in range(n):
        a, b = map(int, input().split())
        if a <= 10 and b > best:
            best = b
            index = i
    print(index + 1)