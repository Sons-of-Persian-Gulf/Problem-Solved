import math

n, k = map(int, input().split())
half = math.ceil(n / 2)
if k <= half:
    print(1 + (k - 1) * 2)
else:
    print(2 + (k - half - 1) * 2)
