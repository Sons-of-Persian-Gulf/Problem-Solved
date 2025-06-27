r, c = map(int, input().split())

pasture = []

for i in range(r):
    pasture.append(list(input()))
# print(pasture)

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def is_is_range(a, b):
    return 0 <= a < r and 0 <= b < c


for i in range(r):
    for j in range(c):
        if pasture[i][j] == "W":
            for r1, c1 in direction:
                x, y = i + r1, j + c1
                if is_is_range(x, y):
                    if pasture[x][y] == "S":
                        print("NO")
                        exit()
                    elif pasture[x][y] == ".":
                        pasture[x][y] = "D"

print("Yes")
for i in pasture:
    print("".join(i))


