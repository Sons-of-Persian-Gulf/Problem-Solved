for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    minimum = min(arr)
    cnt = 0
    for i in arr:
        cnt += i - minimum
    print(cnt)