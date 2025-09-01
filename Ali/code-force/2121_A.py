for _ in range(int(input())):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    first = arr[0]
    last = arr[-1]
    
    if first == last:
        print(abs(s - first))
    elif s < first:
        print(last - s)
    elif s > last:
        print(s - first)
    else:
        left = abs(s - first)
        right = abs(s - last)
        print(min(left, right) * 2 + max(left, right))

