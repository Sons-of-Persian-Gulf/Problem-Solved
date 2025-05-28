from collections import Counter
for _ in range(int(input())):
    n = int(input())
    c = Counter(input().split())
    cnt = 0
    for x, y in c.items():
        if int(y) >= 3:
            print(x)
            break
    else:
        print(-1)
    # print(cnt if cnt else -1)


