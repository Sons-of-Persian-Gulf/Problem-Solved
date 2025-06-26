from collections import defaultdict
n, m = map(int, input().split())

colors = list(map(int, input().split()))
neighbors = defaultdict(set)
present = set(colors)
for _ in range(m):
    u, v = map(int, input().split())
    cv, cu = colors[v - 1], colors[u - 1]

    if cv != cu:
        neighbors[cv].add(cu)
        neighbors[cu].add(cv)

# print(present)
# print(neighbors)
best_count = -1
best_color = None
for c in present:
    cnt = len(neighbors[c])
    if cnt > best_count or (cnt == best_color and best_color is None or c < best_color):
        best_color = c
        best_count = cnt
print(best_color)


