from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = ""
    for _ in range(n):
        s += input()

    c = Counter(s)
    for i, j in c.items():
        if j % n != 0:
            print("NO")
            break
    else:
        print("YES")
            
    