import math
for _ in range(int(input())):
    r, b, d = map(int, input().split())
    m = min(r, b)
    r = math.ceil(r / m)
    b = math.ceil(b / m)

    print("YES" if abs(r - b) <= d else "NO")
