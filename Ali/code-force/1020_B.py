n = int(input())
arr = list(map(int, input().split()))

edges = [[] for _ in range(n + 1)]

for i in range(n):
    edges[i + 1].append(arr[i])

ans = []


def dfs(node):
    c = [0] * (n + 1)
    c[node] += 1
    stack = [node]
    while stack:
        node = stack.pop()
        for neighbor in edges[node]:
            c[neighbor] += 1
            if c[neighbor] == 2:
                ans.append(str(neighbor))
                break
            stack.append(neighbor)


for i in range(1, n + 1):
    dfs(i)

print(" ".join(ans))