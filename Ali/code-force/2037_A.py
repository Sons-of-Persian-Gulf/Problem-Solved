from collections import Counter
for _ in range(int(input())):
    n = int(input())
    c = Counter(input().split())

    cnt = 0
    for i, j in c.items():
        cnt += j // 2

    print(cnt)
