for _ in range(int(input())):
    n = int(input())
    s = input()
    ask = set("Timur")
    cnt = 0
    if n != 5:
        print("NO")
    else:
        if set(s) == set("Timur"):
            print("YES")
        else:
            print("NO")

