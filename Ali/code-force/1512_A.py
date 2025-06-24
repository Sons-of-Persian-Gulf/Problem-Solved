for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    i = 0
    for i in range(0, n - 2):
        x = arr[i]
        if x == arr[i + 1] and x == arr[i + 2]:
            continue
        else:
            if x == arr[i + 1]:
                print(i + 3)
            elif x == arr[i + 2]:
                print(i + 2)
            else:
                print(i + 1)
            break




