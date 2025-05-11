s = "abcdefghijklmnopqrstuvwxyz"
for _ in range(int(input())):
    n = int(input())
    found = False
    for i in range(1, 27):
        for j in range(1, 27):
            x = n - i - j
            if 1 <= x <= 26 and n == x + i + j:
                print(f"{s[i - 1]}{s[j - 1]}{s[x - 1]}")
                found = True
                break
        if found:
            break

