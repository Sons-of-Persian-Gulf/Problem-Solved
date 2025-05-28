x, y = 1, 1
for _ in range(int(input())):
    n = int(input())
    s = input()
    cx, cy = 0, 0
    for i in s:
        if i == "R":
            cx += 1
        elif i == "L":
            cx -= 1
        elif i == "U":
            cy += 1
        else:
            cy -= 1
        if cx == x and y == cy:
            print("YES")
            break
    else:
        print("NO")