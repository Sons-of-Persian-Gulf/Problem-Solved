from collections import Counter
for _ in range(int(input())):
    s = Counter(input())
    a = s["A"]
    b = s["B"]
    c = s["C"]
    if a + c == b:
        print("YES")
    else:
        print("NO")
    