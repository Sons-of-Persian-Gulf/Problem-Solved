n, m = map(int, input().split())


edges = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)


visited = [False] * (n + 1)


def dfs(node):
    visited[node] = True
    stack = [node]
    while stack:
        node = stack.pop()
        for neighbor in edges[node]:
            if not visited[neighbor]:
                stack.append(neighbor)
                dfs(neighbor)


cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)

if cnt == 1 and n == m:
    print("FHTAGN!")
else:
    print("NO")
