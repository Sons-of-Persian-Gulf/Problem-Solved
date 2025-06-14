t = int(input())
for _ in range(t):
    s = list(input().strip())
    n = len(s)
    if n == 0:
        print("")
        continue

    # If first and last match → already balanced
    if s[0] == s[-1]:
        print("".join(s))
    else:
        # Change last to match first
        s[-1] = s[0]
        print("".join(s))

