import sys
sys.setrecursionlimit(10**5 + 10)

def dfs(node, visited):
    visited[node] = True
    for neighbor in edges[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited)

def is_graph_connected(n):
    visited = [False] * n
    dfs(0, visited)
    return all(visited)

# Input
n, m = map(int, input().split())
edges = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

# Degree of each node
degree = [len(adj) for adj in edges]

# Count of each degree
d1 = degree.count(1)
d2 = degree.count(2)
d_star = degree.count(n - 1)

# Connectivity check
is_conn = is_graph_connected(n)

# Topology detection
if is_conn and d1 == 2 and d2 == n - 2:
    print("bus topology")
elif is_conn and d2 == n:
    print("ring topology")
elif is_conn and d1 == n - 1 and d_star == 1:
    print("star topology")
else:
    print("unknown topology")
