for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    longest = 0
    cnt = 0
    for i in range(n):
        if arr[i] == 0:
            cnt += 1
        else:
            if cnt > longest:
                longest = cnt
            cnt = 0
    print(max(longest, cnt))
