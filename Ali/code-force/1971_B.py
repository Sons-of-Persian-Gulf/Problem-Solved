n = int(input())
for _ in range(n):
    s = list(input())
    flag = False
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            s[i], s[i - 1] = s[i - 1], s[i]
            flag = True
            break
    if flag:
        print("YES")
        print("".join(s))
    else:
        print("NO")
