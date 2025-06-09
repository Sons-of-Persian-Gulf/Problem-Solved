import math

for _ in range(int(input())):
    n, k = map(int, input().split())
    x = n % math.gcd(2, k) == 0
    if x:
        print("YES")
    else:
        print("NO")
