arr = list(map(int, input().split()))
s = set()
cnt = 0
for i in arr:
  if i in s:
    cnt += 1
  else:
    s.add(i)
print(cnt)