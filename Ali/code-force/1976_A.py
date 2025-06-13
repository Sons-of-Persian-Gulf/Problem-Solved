for _ in range(int(input())):
    n = int(input())
    s = input()
    digit = 0
    alp = "a"
    for i in range(0, n):
        if i != 0 and s[i].isdigit() and s[i - 1].isalpha():
            print("NO")
            break
        if not s[i].isalnum():
            print("NO")
            break
        if s[i].isdigit():
            if int(s[i]) >= digit:
                digit = int(s[i])
            else:
                print("NO")
                break
        if s[i].isalpha():
            if ord(s[i]) >= ord(alp):
                alp = s[i]
            else:
                print("NO")
                break

    else:
        print("YES")
