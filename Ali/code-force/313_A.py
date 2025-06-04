n = int(input())

if n >= 0:
    print(n)
else:
    a = int(str(n)[:-1])
    b = int(str(n)[:-2] + str(n)[-1:])
    if a > b:
        print(a)
    else:
        print(b)
