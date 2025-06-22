n = int(input())

ans = "I"

i = 1
while i <= n:
    if i % 2 == 0:
        ans += " love"
    else:
        ans += " hate"
    if i + 1 <= n:
        ans += " that I"
    i += 1


ans += " it"
print(ans)