n = int(input())
while True:
    s = 0
    for i in str(n):
        s += int(i)
    if s % 4 == 0:
        break
    n += 1
print(n)
