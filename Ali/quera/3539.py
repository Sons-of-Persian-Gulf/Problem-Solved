s = input()
ans = 0

while True:
    for i in s:
        ans += int(i)
    if ans <= 9:
        print(ans)
        break
    s = str(ans)
    ans = 0




