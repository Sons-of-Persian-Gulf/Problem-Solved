for _ in range(int(input())):
    x = int(input())
    if x < 7 or x == 9:
        print("NO")
    else:
        if x % 3 != 0:
            print("YES")
            print(1, 2, x - 3)
        elif x % 3 == 0:
            print("YES")
            print(1, 4, x - 5)
        else:
            print("NO")
