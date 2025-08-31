import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    candies.sort()
    max1 = candies[-1]
    if n == 1:
        print("YES" if max1 == 1 else "NO")
    else:
        max2 = candies[-2]
        print("NO" if max1 - max2 > 1 else "YES")
