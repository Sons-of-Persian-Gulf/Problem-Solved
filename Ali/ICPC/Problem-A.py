m, d = map(int, input().split())

year, month, day = map(int, input().split())

day += 1
if day > d:
    day = 1
    month += 1
if month > m:
    month = 1
    year += 1
print(year, month, day)
    