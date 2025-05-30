import sys
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, m = map(int, input().split())
countries_power = [0] + list(map(int, input().split()))
edges = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)


def solve(start):
    visited = [False] * (n + 1)
    power = countries_power[start]
    extra = 0
    visited[start] = True
    count = 1

    min_heap = []
    for neighbor in edges[start]:
        if not visited[neighbor]:
            heapq.heappush(min_heap, (countries_power[neighbor], neighbor))

    while count < n and min_heap:
        p, node = heapq.heappop(min_heap)
        if visited[node]:
            continue
        if power <= p:
            need = p - power + 1
            extra += need
            power += need + p
        else:
            power += p
        visited[node] = True
        count += 1
        for neighbor in edges[node]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (countries_power[neighbor], neighbor))

    return extra


result = [str(solve(i)) for i in range(1, n + 1)]
print(" ".join(result))
