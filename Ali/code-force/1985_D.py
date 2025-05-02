for _ in range(int(input())):
    r, h = map(int, input().split())
    arr = []
    for _ in range(r):
        arr.append(list(input()))
    
    tx = -1
    ty = -1
    found = False
    bx = -1
    by = -1

    for i in range(r):
        for j in range(h):
            if arr[i][j] == "#":
                tx = i + 1
                ty = j + 1
                found = True
                break
        if found:
            break

    found = False

    for i in range(r - 1, -1, -1):
        for j in range(h - 1, -1, -1):
            if arr[i][j] == "#":
                bx = i + 1
                by = j + 1
                found = True
                break
        if found:
            break
    if tx == bx:
        print(tx, ty)
    else:
        print(((tx + bx) // 2), ((ty + by) // 2))
    