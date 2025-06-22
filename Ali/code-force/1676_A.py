for _ in range(int(input())):
    s = list(map(int, list(input())))
    if sum(s[:3]) == sum(s[-3:]):
        print("Yes")
    else:
        print("No")