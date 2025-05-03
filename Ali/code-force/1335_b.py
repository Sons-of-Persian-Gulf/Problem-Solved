letters = "abcdefghijklmnopqrstuvwxyz"
for _ in range(int(input())):
    n, a, b = map(int, input().split())
    i = 0
    ans = ""
    while n != 0:
        ans += letters[i]
        i += 1
        n -= 1
        if i == b:
            i = 0
    print(ans)

    # n, a, b = map(int, input().split())
    #     pattern = ''.join(chr(ord('a') + i) for i in range(b))
    #     result = (pattern * ((n // len(pattern)) + 1))[:n]
    #     print(result)