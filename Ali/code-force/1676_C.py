def difference(a, b, size):
    cnt = 0
    for i in range(size):
        cnt += abs(ord(a[i]) - ord(b[i]))
    return cnt

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(input())
    best = float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            x = difference(arr[i], arr[j], m)
            if x < best:
                best = x
    print(best)
