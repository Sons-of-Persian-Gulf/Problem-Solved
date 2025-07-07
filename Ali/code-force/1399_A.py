for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    if n == 1 or (n == 2 and arr[1] - arr[0] <= 1):
        print("YES")
    else:
        index = n - 1
        for _ in range(n - 1):
            if arr[index] - arr[index - 1] <= 1:
                arr.pop()
                index -= 1
        if len(arr) == 1:
            print("YES")
        else:
            print("NO")


# for _ in range(int(input())):
#     n = int(input())
#     arr = sorted(map(int, input().split()))
#     ok = True
#     for i in range(1, n):
#         if arr[i] - arr[i - 1] > 1:
#             ok = False
#             break
#     print("YES" if ok else "NO")
