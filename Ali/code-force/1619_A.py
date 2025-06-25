for _ in range(int(input())):
    s = input()
    n = len(s)
    if n % 2 != 0:
        print("NO")
    else:
        n = n // 2
        s1 = s[:n]
        s2 = s[n:]
        print("YES" if s1 == s2 else "NO")

