for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    flag = True
    for i in range(0, n - 1):
        if arr[i + 1] <= arr[i]:
            flag = False
    print("YES" if flag else "NO")