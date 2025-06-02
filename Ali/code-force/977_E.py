n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)


visited = [False] * (n + 1)


def dfs(node):
    s = {node}
    visited[node] = True
    stack = [node]
    while stack:
        node = stack.pop()
        for neighbor in edges[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                s.add(neighbor)
                stack.append(neighbor)
    return s


node_in_component = []
connected_cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        connected_cnt += 1
        node_in_component.append(dfs(i))

cnt = 0

for component in node_in_component:
    if len(component) < 3:
        continue
    elif len(component) >= 3:
        flag = True
        for i in component:
            if len(edges[i]) != 2:
                flag = False
                break
        if flag:
            cnt += 1

print(cnt)

