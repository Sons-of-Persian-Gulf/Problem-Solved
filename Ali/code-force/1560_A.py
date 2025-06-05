arr = [0] * 1001

cnt = 0
i = 1
while cnt <= 1000:
    if not (i % 3 == 0 or i % 10 == 3):
        arr[cnt] = i
        cnt += 1
    i += 1


for _ in range(int(input())):
    n = int(input())
    print(arr[n - 1])
