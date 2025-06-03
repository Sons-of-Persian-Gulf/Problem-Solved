n, k = map(int, input().split())
a = list(map(int, input().split()))

eligible = 0
for x in a:
    if x + k <= 5:
        eligible += 1

print(eligible // 3)


# from collections import Counter
# n, k = map(int, input().split())
#
#
# p = Counter(map(int, input().split()))
#
# if k == 1:
#     print((p[0] + p[1] + p[2] + p[3] + p[4]) // 3)
# elif k == 2:
#     print((p[0] + p[1] + p[2] + p[3]) // 3)
# elif k == 3:
#     print((p[0] + p[1] + p[2]) // 3)
# elif k == 4:
#     print((p[0] + p[1]) // 3)
# elif k == 5:
#     print((p[0]) // 3)

