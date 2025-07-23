def can_shower(n, s, m, intervals):
    if intervals[0][0] >= s:
        return True
    for i in range(1, n):
        if intervals[i][0] - intervals[i - 1][1] >= s:
            return True
    if m - intervals[-1][1] >= s:
        return True
    return False

for _ in range(int(input())):
    n, s, m = map(int, input().split())
    intervals = [tuple(map(int, input().split())) for _ in range(n)]

    if can_shower(n, s, m, intervals):
        print("YES")
    else:
        print("NO")
    

    