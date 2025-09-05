for _ in range(int(input())):
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    arr = [a, b, c, d]

    if arr.count(1) in [4]:
        print(2)
    elif arr.count(1) in [1, 2, 3]:
        print(1)
    else:
        print(0)