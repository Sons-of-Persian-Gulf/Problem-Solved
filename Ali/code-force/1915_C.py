import math

for _ in range(int(input())):
    n = int(input())
    x = sum(list(map(int, input().split())))
    # print(x, math.sqrt(x), int(math.sqrt(x)) ** 2)
    flag = x == int(math.sqrt(x)) ** 2
    print("YES" if flag else "NO")