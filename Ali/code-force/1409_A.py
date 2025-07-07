import math

for _ in range(int(input())):
    a, b = map(int, input().split())
    # if a == b:
    #     print(0)
    # else:
    #     x = abs(a - b)
    #     cnt = 0
    #     while x != 0:
    #         for i in range(10, 0, -1):
    #             if x >= i:
    #                 a = x // i
    #                 x -= a * i
    #                 cnt += a
    #                 break
    #     print(cnt)
    print(math.ceil(abs(a - b) / 10))
