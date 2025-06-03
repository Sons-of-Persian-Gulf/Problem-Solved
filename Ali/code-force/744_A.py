n, m, k = map(int, input().split())

home = list(map(int, input().split()))


edges = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())

    edges[u].append(v)
    edges[v].append(u)

visited = [False] * (n + 1)

components = []


def dfs(node):
    visited[node] = True
    stack = [node]
    count = 1
    has_special = node in home

    while stack:
        x = stack.pop()
        for neighbor in edges[x]:
            if not visited[neighbor]:
                visited[neighbor] = True
                count += 1
                if neighbor in home:
                    has_special = True
                stack.append(neighbor)

    return (count, has_special)


for i in range(1, n + 1):
    if not visited[i]:
        size, has_spec = dfs(i)
        components.append((size, has_spec))
# print(components)
# Separate special and non-special components
special_comps = [x for x in components if x[1]]
non_special_total = sum(x[0] for x in components if not x[1])

# Add all non-special nodes to the largest special component
special_comps.sort(reverse=True)  # largest special comp first
special_comps[0] = (special_comps[0][0] + non_special_total, True)
# print(special_comps)

# Calculate total max edges
total = 0
for size, _ in special_comps:
    total += size * (size - 1) // 2


print(total - m)

