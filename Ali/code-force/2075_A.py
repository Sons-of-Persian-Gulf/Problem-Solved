import math
for _ in range(int(input())):
    n, k = map(int, input().split())
    cnt = 0
    if n % 2 == 1:
        if k % 2 == 1:
            n -= k
            k -= 1
        else:
            k -= 1
            n -= k
        cnt += 1
        print(cnt + math.ceil(n / k))
    else:
        if k % 2 == 1:
            print(math.ceil(n / (k - 1)))
        else:
            print(math.ceil(n / k))
            
            
    
            