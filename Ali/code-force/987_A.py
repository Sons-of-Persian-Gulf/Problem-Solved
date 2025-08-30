
n = int(input())
arr = list(map(int, input().split()))
k = set()
result = []
for i in range(n - 1, -1, -1):
    if arr[i] not in k:
        result.append(arr[i])
        k.add(arr[i])
print(len(result))
print(*result[::-1])