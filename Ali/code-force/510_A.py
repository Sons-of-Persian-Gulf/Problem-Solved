n, m = map(int, input().split())
j = 0
for i in range(n):
    if j == 0 or j == 2:
        print("#" * m)
    elif j == 1:
        print("." * (m - 1) + "#")
    elif j == 3:
        print("#" + "." * (m - 1))
    elif j == 4:
        j = 0
        print("#" * m)
    j += 1
