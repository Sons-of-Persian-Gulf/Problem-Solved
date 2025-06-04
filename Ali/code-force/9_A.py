import math

y, w = map(int, input().split())
max_roll = max(y, w)
favorable = 6 - max_roll + 1
g = math.gcd(favorable, 6)

print(f"{favorable // g}/{6 // g}")

