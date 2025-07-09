for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int,input().split()))
    start = arr[0]
    last = (x - arr[n - 1]) * 2
    if n == 1:
        print(max(start, last))
    else:
        m = -float("inf")
        for i in range(0, n - 1):
            if arr[i + 1] - arr[i] > m:
                m = arr[i + 1] - arr[i]
        print(max(m, last, start))
