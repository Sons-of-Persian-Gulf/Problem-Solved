for _ in range(int(input())):
    a, b = input().split()
    if a == b:
        print("=")
    else:
        x1 = a.count("X") + 1
        x2 = b.count("X") + 1
        if a[-1] == "L":
            size1 = 1 * x1
        if b[-1] == "L":
            size2 = 1 * x2
        if a[-1] == "S":
            size1 = -1 * x1
        if b[-1] == "S":
            size2 = -1 * x2
        if a[-1] == "M":
            size1 = 0
        if b[-1] == "M":
            size2 = 0
        # print(size1, size2)
        if size1 > size2:
            print(">")
        else:
            print("<")
