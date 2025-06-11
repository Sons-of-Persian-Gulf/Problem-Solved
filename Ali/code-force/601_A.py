from collections import deque


def bfs(graph, start, end, n):
    visited = [False] * (n + 1)
    dist = [0] * (n + 1)

    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        if node == end:
            return dist[node]
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return -1  # No path found


n, m = map(int, input().split())

rails = [[] for _ in range(n + 1)]
roads = [[] for _ in range(n + 1)]

for i in range(1, m + 1):
    u, v = map(int, input().split())
    rails[u].append(v)
    rails[v].append(u)


for u in range(1, n + 1):
    for v in range(1, n + 1):
        if u != v and v not in rails[u]:
            roads[u].append(v)

# Choose which graph to travel on:
if n in rails[1]:  # if rail exists directly
    distance = bfs(roads, 1, n, n)
else:
    distance = bfs(rails, 1, n, n)

print(distance)
