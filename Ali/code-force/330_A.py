r, c = map(int, input().split())
arr = []
for i in range(r):
    arr.append(list(input()))

cnt_1 = 0
cnt_2 = 0
for i in range(r):
    if 'S' not in arr[i]:
        cnt_1 += 1
for i in range(c):
    x = ""
    for j in range(r):
        x += arr[j][i]
    if 'S' not in x:
        cnt_2 += 1
print(cnt_1 * c + cnt_2 * (r - cnt_1))