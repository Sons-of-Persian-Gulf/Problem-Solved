for _ in range(int(input())):
    n, j, k = map(int, input().split())
    arr = list(map(int, input().split()))
    m = max(arr)

    if m == arr[j - 1] or k >= 2:
        print("YES")
    else:
        print("NO")
