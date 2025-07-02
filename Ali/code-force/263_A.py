arr = [list(map(int, input().split())) for _ in range(5)]


for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:
            print(abs((i + 1) - 3) + abs((j + 1) - 3))