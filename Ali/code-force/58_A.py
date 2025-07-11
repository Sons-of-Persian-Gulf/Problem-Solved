word = "hello"
cnt = 0
s = input()

for i in s:
    if i == word[cnt]:
        cnt += 1
    if cnt > 4:
        break

print("YES" if cnt == 5 else "NO")

