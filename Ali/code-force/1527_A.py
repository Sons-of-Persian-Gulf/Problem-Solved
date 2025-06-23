for _ in range(int(input())):
    n = int(input())

    if n == 1:
        print(0)
    else:
        print(int((len(bin(n)[2:]) - 1) * "1", 2))
    # for i in range(n - 1, -1, -1):
    #     n &= i
    #     if n == 0:
    #         print(i)
    #         break
# import math
#
# t = int(input())
# for _ in range(t):
#     n = int(input().strip())
#     if n == 0:
#         print(0)
#         continue
#     msb = n.bit_length() - 1
#     k = (1 << msb) - 1
#     print(k)

