n, m = map(int, input().split())

# Vasya can keep going: initial days = n, plus extra days from loss intervals
extra_days = (n - 1) // (m - 1)
print(n + extra_days)
