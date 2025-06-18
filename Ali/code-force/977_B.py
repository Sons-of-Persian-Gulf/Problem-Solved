n = int(input())
s = input()
d = dict()
for i in range(n - 1):
    x = s[i] + s[i + 1]
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
best = 0
current = ""
for i, j in d.items():
    if j > best:
        best = j
        current = i

print(current)