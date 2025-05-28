for _ in range(int(input())):
    ans = ""
    for _ in range(int(input())):
        x = input()
        for i in range(4):
            if x[i] == "#":
                ans += f"{i + 1} "
    print(ans[::-1].strip())
