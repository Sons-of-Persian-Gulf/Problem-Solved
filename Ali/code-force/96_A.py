s = input()
cnt0 = 0
cnt1 = 0
flag = False
for i in s:
    if i == "0":
        cnt0 += 1
        cnt1 = 0
    else:
        cnt1 += 1
        cnt0 = 0
    if cnt1 >= 7 or cnt0 >= 7:
        flag = True

print("YES" if flag else "NO")
