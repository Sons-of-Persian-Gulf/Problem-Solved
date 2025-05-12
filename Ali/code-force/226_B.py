n, t = map(int, input().split())
arr = list(input())
cnt = 0

while cnt < t:
    i = 0
    while i < n -1:
        if arr[i] == "B" and arr[i + 1] == "G":
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i += 1
        i += 1
    cnt += 1
print("".join(arr))


