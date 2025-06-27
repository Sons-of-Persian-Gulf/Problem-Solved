n, m = map(int, input().split())

in_degree = [0] * (n + 1)
adj = [None] * (n + 1)
nxt = [0] * (n + 1)
diam = [0] * (n+1)

for _ in range(m):
    a, b, d = map(int, input().split())
    in_degree[b] = 1
    adj[a] = b
    diam[a] = d

visited = [False] * (n + 1)
result = []


def dfs(u):
    min_d = float("inf")
    start = u
    while adj[u] and not visited[u]:
        visited[u] = True
        min_d = min(min_d, diam[u])
        u = adj[u]

    visited[u] = True
    return start, u, min_d


for i in range(1, n + 1):
    if not visited[i] and in_degree[i] == 0 and adj[i]:
        result.append(dfs(i))


print(len(result))
for s, t, d in result:
    print(s, t, d)

