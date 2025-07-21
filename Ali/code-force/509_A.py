n = int(input())

if n == 1:
    print(1)
else:
        
    arr = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            arr[i][j] = arr[i][j - 1] + arr[i - 1][j]
    print(arr[n - 1][n - 1])