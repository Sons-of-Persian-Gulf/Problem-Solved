for _ in range(int(input())):
    n = int(input())
    ans = ""
    s = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    for i in s:
        if n >= i:
            ans += str(i)
            n -= i
    print(ans[::-1])