import math
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    plus = 0
    minus = 0
    for i in arr:
        if i == 1:
            plus += 1
        else:
            minus += 1
    cnt = 0
    if plus < minus:
            d = (n // 2) - plus + (n % 2)
            plus += d
            minus -= d
            cnt += d
    if minus % 2 != 0:
        minus -= 1
        plus += 1
        cnt += 1

    
    
    print(cnt)
   
    