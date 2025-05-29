import sys
sys.setrecursionlimit(1_000_000)  # Increased further for safety

def solve():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def in_bounds(x, y):
        return 0 <= x < n and 0 <= y < m

    def dfs(x, y):
        visited[x][y] = True
        stack = [(x, y)]
        total = grid[x][y]

        while stack:
            cx, cy = stack.pop()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if in_bounds(nx, ny) and not visited[nx][ny] and grid[nx][ny] != 0:
                    visited[nx][ny] = True
                    total += grid[nx][ny]
                    stack.append((nx, ny))
        return total

    max_volume = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0 and not visited[i][j]:
                max_volume = max(max_volume, dfs(i, j))

    print(max_volume)


# Read number of test cases
t = int(input())
for _ in range(t):
    solve()
