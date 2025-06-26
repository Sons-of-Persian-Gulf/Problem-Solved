for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        print(2 * a * 2 * b)
    elif 2 * a == b or 2 * b == a:
        print(max(a, b) ** 2)
    elif a < b < 2 * a:
        print((2 * a) ** 2)
    elif b < a <= 2 * b:
        print((2 * b) ** 2)
    else:
        print(max(a, b) ** 2)
    # elif a < b <= 2 * a:
    #     print(2 * a * 2 * a)
    # else:
    #     print(2 * b * 2 * b)
    # print(max(2 * a, b) * max(2 * b, a))
