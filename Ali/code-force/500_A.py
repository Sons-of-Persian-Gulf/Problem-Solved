n, t = map(int, input().split())
arr = list(map(int, input().split()))

edges = [[] for _ in range(n + 1)]


for i in range(len(arr)):
    edges[i + 1].append(arr[i] + i + 1)


visited = [False] * (n + 1)


def dfs(node):
    stack = [node]
    visited[node] = True
    while stack:
        node = stack.pop()
        if node == t:
            return True
        for neighbor in edges[node]:
            if not visited[neighbor]:
                stack.append(neighbor)
    return False


if dfs(1):
    print("YES")
else:
    print("NO")
print()


