n, l = map(int, input().split())
lanterns = sorted(map(int, input().split()))
r = -float("inf")
for i in range(1, n):
    x = (lanterns[i] - lanterns[i - 1]) / 2
    if x > r:
        r = x

print(max(lanterns[0], l - lanterns[n - 1], r))

