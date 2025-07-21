from collections import Counter
for _ in range(int(input())):
    n, m = map(int, input().split())
    s = Counter(input())
    cnt = 0
    for i in "ABCDEFG":
        a = s[i] - m
        if a < 0:
            cnt += abs(a)

    print(cnt)

    
