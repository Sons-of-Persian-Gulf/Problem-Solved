t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    seen = dict()
    ok = True

    for i, char in enumerate(s):
        parity = i % 2
        if char in seen:
            if seen[char] != parity:
                ok = False
                break
        else:
            seen[char] = parity

    print("YES" if ok else "NO")
