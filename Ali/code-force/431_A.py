a1, a2, a3, a4 = map(int, input().split())


cnt = 0
for i in input():
    if i == "1":
        cnt += a1
    elif i == "2":
        cnt += a2
    elif i == "3":
        cnt += a3
    else:
        cnt += a4

print(cnt)





