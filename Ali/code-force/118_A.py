vowel = ["A", "O", "Y", "E", "U", "I"]
ans = ""
s = input()

for i in s:
    if i.upper() in vowel:
        continue
    ans += f".{i.lower()}"

print(ans)