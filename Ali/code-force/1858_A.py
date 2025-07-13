for _ in range(int(input())):
    a, b, c = map(int, input().split())

    

    turn = c % 2
    x = min(a, b)
    a -= x
    b -= x
    while True:
        if turn % 2 == 0:
            if a > 0:
                a -= 1
            else:
                print("Second")
                break
        else:
            if b > 0:
                b -= 1
            else:
                print("First")
                break
        if turn == 0:
            turn = 1
        else:
            turn = 0
    