for _ in range(int(input())):
    n ,k = map(int, input().split())
    d = dict()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n):
        if a[i] in d:
            d[a[i]] += b[i]
        else:
            d[a[i]] = b[i]

    
    for i, j in sorted(d.items(), key=lambda x: x[0]):
        if k >= i:
            k += j
    print(k)