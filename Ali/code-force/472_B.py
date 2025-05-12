import bisect
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
j = list(map(int, input().split()))


for i in range(1, n):
    arr[i] += arr[i - 1]


for q in j:
    print(bisect.bisect_left(arr, q) + 1)


