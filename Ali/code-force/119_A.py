import math
a, b, n = map(int, input().split())

i = 0
while n != 0:
    if i % 2 == 0:
        n -= math.gcd(a, n)
    else:
        n -= math.gcd(b, n)
    i += 1
    
print((i + 1) % 2)