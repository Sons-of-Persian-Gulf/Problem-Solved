import math

n, m = map(int, input().split())

# Maximum isolated vertices: if each edge connects two different people
max_isolated = max(0, n - 2 * m)

# Minimum isolated vertices: find smallest x such that x(x-1)/2 >= m
if m == 0:
    min_isolated = n
else:
    x = math.ceil((1 + math.sqrt(1 + 8 * m)) / 2)
    min_isolated = n - x

print(max_isolated, min_isolated)
