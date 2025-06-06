row1 = input().split()
row2 = input().split()

cnt = 0
for i in range(8):
    if row1[i] == "1" and row2[i] == "1":
        cnt += 1
print(cnt)