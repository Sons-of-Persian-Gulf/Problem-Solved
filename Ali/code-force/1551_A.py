# for _ in range(int(input())):
#     n = int(input())
#     x = n // 3
#     best = float("inf")
#     num1 = 0
#     num2 = 0
#     for i in range(x - 2, x + 2):
#         for j in range(x - 2, x + 2):
#             if i + j * 2 == n:
#                 if abs(i - j) < best:
#                     best = abs(i - j)
#                     num1 = i
#                     num2 = j
#
#     print(num1, num2)
t = int(input())
for _ in range(t):
    n = int(input())
    k = n // 3
    remainder = n % 3

    if remainder == 0:
        print(k, k)
    elif remainder == 1:
        print(k + 1, k)
    else:  # remainder == 2
        print(k, k + 1)

