a = "qwertyuiop"
b = "asdfghjkl;"
c = "zxcvbnm,./"
ans = ''
shift = -1 if input() == "R" else 1
s = input()
for i in s:
    for j in range(10):
        if a[j] == i:
            ans += a[j + shift]
        elif b[j] == i:
            ans += b[j + shift]
        elif c[j] == i:
            ans += c[j + shift]
print(ans)