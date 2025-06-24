n = int(input())
arr = list(map(int, input().split()))

# Find index of max (leftmost) and min (rightmost)
max_i = arr.index(max(arr))
min_i = n - 1 - arr[::-1].index(min(arr))

if max_i > min_i:
    print(max_i + (n - 1 - min_i) - 1)
else:
    print(max_i + (n - 1 - min_i))


# n = int(input())
#
# arr = list(map(int, input().split()))
#
# index = -1
# height = -1
# cnt = 0
# for i in range(n):
#     if arr[i] > height:
#         height = arr[i]
#         index = i
#
# for i in range(index, 0, -1):
#     arr[i], arr[i - 1] = arr[i - 1], arr[i]
#     cnt += 1
#
# for i in range(n - 1, -1, -1):
#     if arr[i] < height:
#         height = arr[i]
#         index = i
# for i in range(index, n - 1):
#     arr[i], arr[i + 1] = arr[i + 1], arr[i]
#     cnt += 1
# print(cnt)
#
# # print(arr)
#
#
#
#
