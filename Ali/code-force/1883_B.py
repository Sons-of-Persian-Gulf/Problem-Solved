from collections import Counter

for _ in range(int(input())):
    n , k = map(int, input().split())
    s = input()
    c = Counter(s)
    
    even = 0
    odd = 0
    for i, j in c.items():
        if j % 2 == 0:
            even += 1
        else:
            odd += 1
    
    if odd <= k + 1:
        print("YES")
    else:
        print("NO")



