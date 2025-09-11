def solve():
    import sys
    input = sys.stdin.readline

    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        from collections import Counter
        cnt = Counter(s)

        if len(cnt) == 1:
            print(-1)
        elif len(cnt) >= 3:
            print(4)
        else:
            # دو رنگ
            freqs = list(cnt.values())
            if 3 in freqs:
                print(6)
            else:
                print(4)

solve()
