for _ in range(int(input())):
    keys = set()
    s = input()
    for i in s:
        if i.islower():
            keys.add(i.upper())
        else:
            if i not in keys:
                print("NO")
                break
    else:
        print("YES")
