import heapq

def dijkstra(n, graph, start):
    dist = [float("inf")] * (n + 1)
    dist[start] = 0
    prev = [-1] * (n + 1)
    pq = [(0, start)] # (distance, vertex)
    while pq:
        d, u = heapq.heappop(pq) # distance, vertex

        if d > dist[u]:
            continue

        for neighbor, weight in graph[u]:
            if dist[neighbor] > dist[u] + weight:
                dist[neighbor] = dist[u] + weight
                prev[neighbor] = u  # track parent
                heapq.heappush(pq, (dist[neighbor], neighbor))

    return dist, prev


def get_path(prev, start, end):
    path = []
    while end != -1:
        path.append(end)
        end = prev[end]
    path.reverse()
    return path if path[0] == start else []


n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    edges[a].append((b, w))
    edges[b].append((a, w))

dist, prev = dijkstra(n, edges, 1)
path = get_path(prev, 1, n)
print(" ".join(map(str, path)) if path else - 1)
    

