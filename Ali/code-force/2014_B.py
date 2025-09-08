import math
for _ in range(int(input())):
    n, k = map(int, input().split())
    start = n - k + 1
    end = n
    if (start % 2 == 1 or end % 2 == 1):
        cnt = math.ceil((end - start) / 2)
        cnt += 1 if (start % 2 == 1 and end % 2 == 1) else 0
    else:
        cnt = (end - start) // 2
    print("YES" if cnt % 2 == 0 else "NO")
    