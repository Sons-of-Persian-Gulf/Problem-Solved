for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    ans = float("inf")
    for i in range(1, n):
        if arr[i] - arr[i - 1] < ans:
            ans = arr[i] - arr[i - 1]
    print(ans)
        