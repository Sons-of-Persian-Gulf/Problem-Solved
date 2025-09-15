import math
for _ in range(int(input())):
    n = int(input())
    s = input()
    print(math.comb((10 - n), 2) * 6)
