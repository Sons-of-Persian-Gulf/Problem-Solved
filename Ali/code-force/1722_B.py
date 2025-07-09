for _ in range(int(input())):
    n = int(input())
    r1 = input()
    r2 = input()
    flag = True
    for i in range(n):
        if r1[i] == r2[i] or (r1[i] == "G" and r2[i] == "B") or (r1[i] == "B" and r2[i] == "G"):
            continue
        else:
            flag = False

    print("YES" if flag else "NO")