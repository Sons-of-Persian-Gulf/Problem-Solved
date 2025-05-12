import math
for _ in range(int(input())):
  a, b = map(int, input().split())
  if a % b == 0:
    print(0)
  else:
    x = a // b + 1
    n = b * x - a
    print(n)
  