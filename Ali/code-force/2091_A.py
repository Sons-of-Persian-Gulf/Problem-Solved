from collections import Counter
for _ in range(int(input())):
    c = Counter("00012235")
    n = int(input())
    s = input().split()
    
    cnt = 8
    index = 0
    for i in range(n):
        if s[i] in c and c[s[i]] > 0:
            c[s[i]] -= 1
            cnt -= 1
            index = i + 1
            if cnt == 0:
                break
    if cnt == 0:
        print(index)
    else:
        print(0)
        
    