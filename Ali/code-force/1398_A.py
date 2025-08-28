for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    a = arr[0]
    b = arr[1]
    c = arr[-1]

    if (a + b > c):
        print(-1)
    else:
        print(1, 2, n)