for _ in range(int(input())):
    r1 = input()
    r2 = input()
    r3 = input()
    x1 = r1[0] == r1[1] and r1[1] == r1[2] and r1[0] in ["X","O", "+"]
    x2 = r2[0] == r2[1] and r2[1] == r2[2] and r2[2] in  ["X","O", "+"]
    x3 = r3[0] == r3[1] and r3[1] == r3[2] and r3[2] in  ["X","O", "+"]
    x4 = r1[0] == r2[1] and r2[1] == r3[2] and r3[2] in ["X","O", "+"]
    x5 = r1[2] == r2[1] and r2[1] == r3[0] and r3[0] in  ["X","O", "+"]
    x6 = r1[0] == r2[0] and r2[0] == r3[0] and r3[0] in ["X","O", "+"]
    x7 = r1[1] == r2[1] and r2[1] == r3[1] and r3[1] in  ["X","O", "+"]
    x8 = r1[2] == r2[2] and r2[2] == r3[2] and r3[2] in  ["X","O", "+"]
    if x1:
        print(r1[0])
    elif x2:
        print(r2[0])
    elif x3:
        print(r3[0])
    elif x4:
        print(r1[0])
    elif x5:
        print(r1[2])
    elif x6:
        print(r1[0])
    elif x7:
        print(r1[1])
    elif x8:
        print(r1[2])
    else:
        print("DRAW")
    