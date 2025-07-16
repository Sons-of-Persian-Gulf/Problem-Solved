n = int(input())
arr = list(map(int, input().split()))

def is_sorted(array, n):
    for i in range(1, n):
        if arr[i] <= arr[i - 1]:
            return False
    return True

increasing = True
l = arr[0]
index = 0
for i in range(1, n):
    if arr[i] < arr[i - 1]:
        index = i - 1
        l = arr[i - 1]
        break

r = l
index2 = index
for i in range(index, n):
    if r < arr[i]:
        break
    r = arr[i]
    index2 = i
# print(l, r)
# print(index, index2)
s1 = index
s2 = index2
while index < index2:
    arr[index], arr[index2] = arr[index2], arr[index]
    index2 -= 1
    index += 1
if is_sorted(arr, n):
    print("yes")
    print(s1 + 1, s2 + 1)
else:
    print("no")
