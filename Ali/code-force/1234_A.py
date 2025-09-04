import math
for _ in range(int(input())):
    n = int(input())
    s = sum(map(int, input().split()))
    print(math.ceil(s / n))