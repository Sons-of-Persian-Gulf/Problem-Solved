a, b = map(int, input().split())
cnt = a
used = a
while used >= b:
    new = used // b
    used = used % b
    cnt += new
    used += new

print(cnt)
