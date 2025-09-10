from collections import Counter
for _ in range(int(input())):
    n = int(input())
    c = Counter(input())
    cnt = 0
    for i, j in c.items():
        if i != "?":
            cnt += min(n, j)
    print(cnt)
    