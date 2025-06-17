for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = ""
    for i in s:
        if i == "D":
            ans += "U"
        elif i == "U":
            ans += "D"
        else:
            ans += i
    print(ans)