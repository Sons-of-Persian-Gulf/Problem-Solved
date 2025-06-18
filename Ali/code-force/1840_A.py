for _ in range(int(input())):
    n = int(input())
    s = input()
    code = ""
    c = s[0]
    i = 1
    while i < n - 1:
        if s[i] == c:
            code += c
            i += 1
            c = s[i]
        i += 1
    print(code + c)
            