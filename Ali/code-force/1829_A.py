s = "codeforces"
for _ in range(int(input())):
    x = input()
    cnt = 0
    for i in range(10):
        if s[i] != x[i]:
            cnt += 1
    print(cnt)
