n = int(input())

edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
colors = [0] + list(map(int, input().split()))

bad = [(u, v) for u, v in edges if colors[u] != colors[v]]




def check(candidate):
    return all(u == candidate or v == candidate for u, v in bad)


if not bad:
    print("YES")
    print(1)
else:
    u0, v0 = bad[0]
    if check(u0):
        print("YES")
        print(u0)
    elif check(v0):
        print("YES")
        print(v0)
    else:
        print("NO")