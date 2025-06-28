a, b = map(int, input().split())

cnt = 0

while not a > b:
    cnt += 1
    a *= 3
    b *= 2

print(cnt)


# import math
#
# a, b = map(int, input().split())
#
# if a > b:
#     print(0)
# else:
#     years = math.ceil(math.log(b / a) / math.log(3 / 2))
#     print(years)
