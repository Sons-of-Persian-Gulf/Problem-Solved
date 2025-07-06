import math

n = int(input())
arr = sorted(list(map(int, input().split())))
# print(arr)
print(arr[math.floor((n - 1) / 2)])
# for i in range(n - 1):
#     if i % 2 == 0:
#         arr.pop()
#     else:
#         arr.pop(0)
#
# print(arr)

