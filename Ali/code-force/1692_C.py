for _ in range(int(input())):
    arr = []
    input()
    # input()
    for i in range(8):
        arr.append(list(input()))
    for i in range(1, 7):
        for j in range(1, 7):
            x1 = arr[i - 1][j - 1] == "#"
            x2 = arr[i - 1][j + 1] == "#"
            x3 = arr[i + 1][j - 1] == "#"
            x4 = arr[i + 1][j + 1] == "#"
            if arr[i][j] == "#" and x1 and x2 and x3 and x4:
                print(i + 1, j + 1)