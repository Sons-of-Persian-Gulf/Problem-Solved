d = dict()
for _ in range(int(input())):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1


max_key = max(d, key=d.get)
print(max_key)