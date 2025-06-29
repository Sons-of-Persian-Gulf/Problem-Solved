n = int(input())
arr = []
for _ in range(2):
    arr.append(input())


edges = [[] for _ in range(2 * n + 1)]
ans = True
for i in range(1, n - 1):
    if arr[0][i] == "X" and (arr[1][i] == "X" or arr[1][i + 1] == "X" or arr[1][i - 1] == "X"):
        ans = False
        break
print("Hooraaay!:))" if ans else "Awww:((")

