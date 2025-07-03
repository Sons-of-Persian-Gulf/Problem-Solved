cnt = 0
for i in (input()):
    if i == "4" or i == "7":
        cnt += 1
print("YES" if cnt == 7 or cnt == 4 else "NO")