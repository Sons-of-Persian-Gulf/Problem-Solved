# n: number of station
# bobs live in neat station 1
# s: goal station
n, s = map(int, input().split())

s -= 1

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


def is_station_after(x):
    for i in range(s + 1, n):
        if i > s and arr1[i] == 1 and arr2[i] == 1:
            return is_way_back(i)
    return False


def is_way_back(x):
    if s < x and arr2[s] == 1:
        return True
    return False


if arr1[0] == 0:
    print("NO")
elif arr1[0] == 1 and arr1[s] == 1:
    print("Yes")
else:
    if is_station_after(s):
        print("YES")
    else:
        print("NO")





