t = int(input())
for _ in range(t):
    n, m, x = map(int, input().split())
    
    # Convert x (1-indexed) to row/column in column-major order
    col = (x - 1) // n + 1
    row = (x - 1) % n + 1
    
    # Convert to row-major position
    ans = (row - 1) * m + col
    print(ans)
