import math
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(math.ceil((abs(a - b) / 2)  / c))