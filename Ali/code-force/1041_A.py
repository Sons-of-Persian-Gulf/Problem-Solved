n = int(input())
arr = list(map(int, input().split()))

max_k = -float("inf")
min_k = float("inf")

for i in arr:
    if i > max_k:
        max_k = i
    if i < min_k:
        min_k = i


print(max_k - min_k + 1 - n)