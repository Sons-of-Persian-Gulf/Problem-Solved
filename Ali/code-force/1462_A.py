for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    i = 0
    j = n - 1
    while i < j:
        print(arr[i], end=" ")
        print(arr[j], end=" ")
        i += 1
        j -= 1
    if n % 2 == 0:
        print()
    else:
        print(arr[i])
