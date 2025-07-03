n = int(input())
i = 0
j = n - 1
arr = list(map(int, input().split()))
turn = "S"
s_points = 0
d_points = 0
while i != j + 1:
    if arr[i] > arr[j]:
        if turn == "S":
            turn = "D"
            s_points += arr[i]
        else:
            turn = "S"
            d_points += arr[i]
        i += 1
    else:
        if turn == "S":
            turn = "D"
            s_points += arr[j]
        else:
            turn = "S"
            d_points += arr[j]
        j -= 1
print(s_points, d_points)



