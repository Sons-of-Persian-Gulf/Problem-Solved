for _ in range(int(input())):
    n = int(input())
    s = input()
    i = n - 1
    ans = ""
    while i >= 0:
        if s[i] == "0":
            x = int(s[i - 2] + s[i - 1])
            ans += chr(x + 96)
            i -= 3
        else:
            x = int(s[i])
            ans += chr(x + 96)
            i -= 1

    print(ans[::-1])
