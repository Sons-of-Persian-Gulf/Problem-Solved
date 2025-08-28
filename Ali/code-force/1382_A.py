from collections import Counter
for _ in range(int(input())):
    n, m = map(int, input().split())
    c = Counter(map(int, input().split()))
    arr = list(map(int, input().split()))
    s = []
    for i in arr:
        if i in c:
            s.append(i)
            break

    length = len(s)
    if length:
        print("YES")
        print(length, *s)
    else:
        print("NO")
    