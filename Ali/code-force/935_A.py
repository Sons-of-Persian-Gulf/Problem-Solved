import math

n = int(input())
cnt = 0

# for i in range(n // 2, 0, -1):
#     if n % i == 0 and ((n // i) - 1) * i + i == n:
#         cnt += 1
# print(cnt)

for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            if i < n:
                cnt += 1
            if n // i != i and n // i < n:
                cnt += 1

print(cnt)