for _ in range(int(input())):
    s = input()
    ans = ""
    for i in s:
        if i == "w":
            ans += i
        elif i == "p":
            ans += "q"
        elif i == "q":
            ans += "p"

    print(ans[::-1])