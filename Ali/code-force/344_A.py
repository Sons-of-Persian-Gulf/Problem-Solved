n = int(input())
s = input()
cnt = 1
for _ in range(n - 1):
    x = input()
    if x != s:
        cnt += 1
        s = x
print(cnt)
