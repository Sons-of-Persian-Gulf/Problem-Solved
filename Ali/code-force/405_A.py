n = int(input())
cols = list(map(int, input().split()))
cols.sort()
print(*cols)
