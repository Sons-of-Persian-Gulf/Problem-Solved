n = int(input())

arr = list(map(int, input().split()))
manpower = 0
untreated = 0
for i in arr:
    if i == -1 and manpower <= 0:
        untreated += 1
    else:
        manpower += i
print(untreated)
