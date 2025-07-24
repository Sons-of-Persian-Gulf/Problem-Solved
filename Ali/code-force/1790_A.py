PI = "314159265358979323846264338327"
for _ in range(int(input())):
    s = input()
    cnt = 0
    for i in range(len(s)):
        if PI[i] != s[i]:
            break
        cnt += 1
    print(cnt)
