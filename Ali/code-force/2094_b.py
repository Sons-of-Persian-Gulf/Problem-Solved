
import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n, m, l, r = map(int, input().split())
    left = (m + 1) // 2
    right = m // 2
    l_p = -left
    r_p = right

    if l_p < l:
        shift = l - l_p
        l_p += shift
        r_p += shift
    elif r_p > r:
        shift = r_p - r
        l_p -= shift
        r_p -= shift

    print(l_p, r_p)
