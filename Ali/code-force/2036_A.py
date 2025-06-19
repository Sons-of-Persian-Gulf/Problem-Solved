for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n - 1):
        if not abs(arr[i] - arr[i + 1]) in [5, 7]:
            print("NO")
            break
    else:
        print("YES")
