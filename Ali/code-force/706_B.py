# n = int(input())
# prices = sorted(list(map(int, input().split())))
# q = int(input())
# dp = [0]
# index = 0
# s = 0
# for i in range(1, prices[-1] + 1):
#     if prices[index] == i:
#         s += 1
#         if index < n - 1:
#             index += 1
#     dp.append(s)
# # print(dp)
# for _ in range(q):
#     print(dp[int(input())])
#     # print("----------")


import bisect

n = int(input())
prices = sorted(map(int, input().split()))
q = int(input())

for _ in range(q):
    x = int(input())
    # price <= x
    print(bisect.bisect_right(prices, x))