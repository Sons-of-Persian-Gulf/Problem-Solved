for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    occupied = set()
    occupied.add(arr[0])
    for i in range(1, n):
        seat = arr[i]
        if (seat - 1 not in occupied) and (seat + 1 not in occupied):
            print("NO")
            break
        occupied.add(seat)
    else:
        print("YES")
