import math

def f(n, s):
    x = int(math.isqrt(n))  # safer than int(sqrt(n))
    if x * x != n:
        return "NO"
    for i in range(x):
        for j in range(x):
            a = s[i * x + j]
            if i == 0 or i == x - 1 or j == 0 or j == x - 1:
                if a != "1":
                    return "NO"
            else:
                if a != "0":
                    return "NO"
    return "YES"
                        
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    print(f(n, s))
