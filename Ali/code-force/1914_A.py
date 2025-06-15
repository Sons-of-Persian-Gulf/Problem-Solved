from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = input()
    c = Counter(s)
    cnt = 0
    for i, j in c.items():
        if ord(i) - 64 <= j:
            cnt += 1
    print(cnt)