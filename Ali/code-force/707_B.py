n, m, k = map(int, input().split())

is_storage = [False] * (n + 1)

edges = []
ans = float('inf')
for i in range(m):
    edges.append(tuple(map(int, input().split())))
# print(edges)
if k > 0:
    for x in map(int, input().split()):
        is_storage[x] = True

    for v, u, w in edges:

        if is_storage[v] ^ is_storage[u]:
            ans = min(ans, w)
    print(ans if ans != float('inf') else -1)
else:
    print(-1)
