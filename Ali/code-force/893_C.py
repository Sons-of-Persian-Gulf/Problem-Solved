import sys
sys.setrecursionlimit(10 ** 6)

# n: number of vertexes
# m: number of edges
n, m = map(int, input().split())

gold_cost = list(map(int, input().split()))

edges = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)


visited = [False] * (n + 1)


# def dfs(node):
#     visited[node] = True
#     min_price = gold_cost[node - 1]
#     for neighbor in edges[node]:
#         if not visited[neighbor]:
#             neighbor_price = dfs(neighbor)
#             min_price = min(min_price, neighbor_price)
#     return min_price


def dfs_stack(node):
    min_cost = gold_cost[node - 1]
    stack = [node]
    visited[node] = True
    while stack:
        node = stack.pop()
        for neighbor in edges[node]:
            if not visited[neighbor]:
                min_cost = min(min_cost, gold_cost[neighbor - 1])
                visited[neighbor] = True
                stack.append(neighbor)
    return min_cost


cnt = 0
cost = 0
for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        cost += dfs_stack(i)


print(cost)

