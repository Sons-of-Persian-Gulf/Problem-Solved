for _ in range(int(input())):
    s = input()
    c = input()
    flag = False
    for i in range(len(s)):
        if c == s[i] and i % 2 == 0:
            flag = True
    print("YES" if flag else "NO")
    # if c == s:
    #     print("YES")
    # elif len(s) == 3 and (c == s[0] or c == s[-1]):
    #     print("YES")
    # elif c in s[2:-2]:
    #     print("YES")
    # else:
    #     print("NO")
