for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())), reverse=True)

    for i in range(min(n, k)):
        if b[i] > a[i]:
            a[i] = b[i]
        else:
            break
    print(sum(a))
    # print(a)
    # print(b)
    # print("\n\n\n-------------------------\n")