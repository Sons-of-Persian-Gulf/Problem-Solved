for _ in range(int(input())):
    n = int(input())
    s = input()
    t = set()
    flag = True
    # ans = ""
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            if s[i] in t:
                flag = False
                break
            t.add(s[i])
            # ans += s[i] + " "
    # print(ans)
    if s[n - 1] in t:
        flag = False
    # print(t)
    print("YES" if flag else "NO")