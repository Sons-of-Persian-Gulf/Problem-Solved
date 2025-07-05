s = input()
letters = set()
cnt = 0
for i in s:
    if i.isalpha() and i not in letters:
        letters.add(i)
        cnt += 1
print(cnt)