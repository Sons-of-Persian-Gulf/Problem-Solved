n, m = map(int, input().split())
tasks = list(map(int, input().split()))
cost = 0
current = 1
for task in tasks:
    if task == current:
        continue
    elif task > current:
        cost += task - current
        current = task
    else:
        cost += n - current + task
        current = task
print(cost)