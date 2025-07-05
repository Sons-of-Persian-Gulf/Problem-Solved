for _ in range(int(input())):
    n = int(input())
    arr = []
    d = 10
    for i in range(len(str(n))):
        x = n % d
        n -= x
        d *= 10
        if x != 0:
            arr.append(x)
    print(len(arr))
    print(" ".join(map(str, arr)))
