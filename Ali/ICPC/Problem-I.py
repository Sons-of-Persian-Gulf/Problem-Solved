n = int(input())

ans = []
for i in range(1, int(n ** .5) + 1):
    if n % i == 0:
        print(i)
        ans.append(n // i)

for i in ans[::-1]:
    print(i)