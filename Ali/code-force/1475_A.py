import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    # If n is not a power of two → it has an odd divisor > 1
    if n & (n - 1):
        print("YES")
    else:
        print("NO")
