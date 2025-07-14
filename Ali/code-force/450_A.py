from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))

queue = deque()
for i in range(n):
    queue.append((i + 1, arr[i]))

current = -1
while queue:
    index, c = queue.popleft()
    if c > m:
        queue.append((index, c - m))
    current = index

print(current)
