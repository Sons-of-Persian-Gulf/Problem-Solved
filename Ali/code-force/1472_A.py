def divide_by_two(n):
    ans = 1
    while n % 2 != 1 and n >= 2:
        n = n / 2
        ans *= 2
    return ans

for _ in range(int(input())):
    w, h, n = map(int, input().split())
    piece = divide_by_two(w) * divide_by_two(h)
    print("YES" if piece >= n else "NO")
