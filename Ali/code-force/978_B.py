n = int(input())
s = input()
cnt = 0
to_remove_cnt = 0
for i in s:
    if i == "x":
        cnt += 1
    else:
        if cnt > 2:
            to_remove_cnt += cnt - 2
        cnt = 0

if cnt > 2:
    to_remove_cnt += cnt - 2

print(to_remove_cnt)