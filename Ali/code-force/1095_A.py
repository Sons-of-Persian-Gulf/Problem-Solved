n = int(input())
ans = ""
s = input()
index = 0
x = 2
while index < n:
    ans += s[index]
    index += x
    x += 1
    

print(ans)

