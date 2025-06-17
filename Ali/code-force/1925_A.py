for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = ""
    for i in range(1, min(k + 1, 27)):
        ans += chr(i + 96)
    # ans += ans[::-1]
    print(ans * n)