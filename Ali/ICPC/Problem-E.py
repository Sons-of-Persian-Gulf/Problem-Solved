# Problem E: In or Out
n = int(input())
ar1 = list(map(int, input().split()))
ar2 = list(map(int, input().split()))
a = max(ar1)
b = min(ar2)

if a > b:
    print(0)
else:
    print(b - a + 1)