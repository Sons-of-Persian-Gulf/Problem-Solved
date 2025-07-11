s = input()

flag = False
for i in s:
    if i in ["H", "Q", "9"]:
        flag = True
        break
print("YES" if flag else "NO")