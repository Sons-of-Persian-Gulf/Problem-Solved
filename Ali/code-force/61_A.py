a = input()
b = input()
ans = ""
for i in range(len(a)):
    if int(a[i]) ^ int(b[i]):
        ans += "1"
    else:
        ans += "0"
print(ans)
