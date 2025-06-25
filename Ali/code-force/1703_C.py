for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        x, s = input().split()
        for j in s:
            if j == "U":
                arr[i] -= 1
                if arr[i] < 0:
                    arr[i] = 9
            else:
                arr[i] += 1
                if arr[i] > 9:
                    arr[i] = 0
    print(" ".join(map(str, arr)))

