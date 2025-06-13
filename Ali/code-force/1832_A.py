from collections import Counter
for _ in range(int(input())):
    c = Counter(input())  # Count characters
    even = 0
    odd = 0
    cnt = 0  # sum of characters with odd frequency
    for i, j in c.items():
        if j % 2 == 0:
            even += 1
        else:
            cnt += j
            odd += 1
    if len(c) == 1:  # only one unique character
        print("NO")
    elif (odd <= 1 and even >= 2) or cnt >= 3:
        print("YES")
    else:
        print("NO")
