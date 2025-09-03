d = {
    "chest": 0,
    "biceps": 0,
    "back": 0,
}

n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    if i % 3 == 0:
        d["chest"] += arr[i]
    elif i % 3 == 1:
        d["biceps"] += arr[i]
    elif i % 3 == 2:
        d["back"] += arr[i]

print(sorted(d.items(), key=lambda x: x[1])[-1][0])
