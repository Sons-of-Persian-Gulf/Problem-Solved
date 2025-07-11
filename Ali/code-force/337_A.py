n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
minimum = float("inf")
# print(arr)
for i in range(m - n + 1):
    x = abs(arr[i + n - 1] - arr[i])
    # print(arr[i], arr[i + n - 1])
    if x < minimum:
        minimum = x

print(minimum)
