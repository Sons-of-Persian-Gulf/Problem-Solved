maximum_capacity = -float("inf")
current = 0

for _ in range(int(input())):
  a, b = map(int, input().split())
  current += b - a
  if current > maximum_capacity:
    maximum_capacity = current
print(maximum_capacity) 