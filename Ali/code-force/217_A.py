# n: number of coordinates
n = int(input())
edges = [[] for _ in range(n)]
coordinates = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if i == j:
            continue
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[j]

        if x1 == x2 or y1 == y2:
            edges[i].append(j)
            edges[j].append(i)

visited = [False] * n
count = 0


def dfs(node):
    visited[node] = True
    for neighbor in edges[node]:
        if not visited[neighbor]:
            dfs(neighbor)


for i in range(n):
    if not visited[i]:
        dfs(i)
        count += 1

print(count - 1)




