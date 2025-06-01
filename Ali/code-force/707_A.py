

n, m = map(int, input().split())

colored = False
for _ in range(n):
    x = list(input().split())
    for i in x:
        if not colored and i in ["C", "Y", "M"]:
            colored = True
            break

if colored:
    print("#Color")
else:
    print("#Black&White")

