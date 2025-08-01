def digit_diff(a, b):
    return sum(x != y for x, y in zip(a, b))


for _ in range(int(input())):
    n = input()
    num = int(n)
    if num % 7 == 0:
        print(num)
    else:
        min_diff = float('inf')
        best = None
        for i in range(0, 1000):
            s = str(i)
            if len(s) != len(n):
                continue
            if i % 7 == 0:
                diff = digit_diff(n, s)
                if diff < min_diff:
                    min_diff = diff
                    best = s
        print(best)
