from itertools import combinations

m = int(input())

arr = [[0 for _ in range(6)] for _ in range(6)]  # 1-indexed

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

# Check all combinations of 3 people out of 5
for i, j, k in combinations(range(1, 6), 3):
    # All friends
    if arr[i][j] and arr[i][k] and arr[j][k]:
        print("WIN")
        exit()
    # None are friends
    if not arr[i][j] and not arr[i][k] and not arr[j][k]:
        print("WIN")
        exit()

# If no such group exists
print("FAIL")
