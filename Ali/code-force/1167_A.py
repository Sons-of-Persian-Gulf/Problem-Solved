for _ in range(int(input())):
    x = int(input())
    s = input()
    if x < 11:
        print("NO")
    elif x == 11:
        print("YES" if s[0] == "8" else "NO")
    else:
        flag = False
        for i in range(x):
            if s[i] == "8":
                if x - i >= 11:
                    flag = True
                break
        print("YES" if flag else "NO")