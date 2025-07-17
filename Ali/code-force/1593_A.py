def f(x, d, cnt):
    if cnt > 1:
        if x == d:
            return(1)
        else:
            return(d - x + 1)
    else:
        if x == d:
            return(0)
        else:
            return(d - x + 1)
        
    

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    d = max(a, b, c)
    cnt = 0
    for i in [a, b, c]:
        if i == d:
            cnt += 1
    print(f(a, d, cnt), f(b, d, cnt), f(c, d, cnt))
        



    