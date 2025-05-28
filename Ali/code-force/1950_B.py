for _ in range(int(input())):
    n = int(input())
    for i in range(1, n + 1):
        ans = ""
        for j in range(1, n + 1):
            if (i + j) % 2 == 0:
                ans += "#" * 2
            else:
                ans += "." * 2
        print(ans)
        print(ans)

