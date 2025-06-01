t = int(input())

for _ in range(t):
    ans = ""
    for _ in range(8):
        s = input()
        for i in s:
            if i != ".":
                ans += i
                break
    print(ans)