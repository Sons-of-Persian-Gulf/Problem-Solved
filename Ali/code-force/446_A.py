n, m, a, b = map(int, input().split())

# Option 1: All rides with single tickets
cost_single = n * a

# Option 2: As many special tickets as possible, remainder with singles
cost_mixed = (n // m) * b + (n % m) * a

# Option 3: Overbuy special tickets to cover all rides
cost_special_only = ((n + m - 1) // m) * b  # same as ceil(n/m) * b

# Minimum of all strategies
print(min(cost_single, cost_mixed, cost_special_only))
