import math

for _ in range(int(input())):
    n = int(input())
    edges = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges[v].append(u)
        edges[u].append(v)
    cnt = sum(1 if len(i) == 1 else 0 for i in edges)

    print(math.ceil(cnt / 2))