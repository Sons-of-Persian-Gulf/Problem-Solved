def not_between(a, b, c):
    return (c > max(a, b) or c < min(a, b))

for _ in range(int(input())):
    input()
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())

    dx = abs(ax - bx)
    dy = abs(ay - by)

    if dx == 0 and not_between(ay, by, cy):
        print(dy)
    elif dy == 0 and not_between(ax, bx, cx):
        print(dx)
    elif dx == 0 and not not_between(ax, bx, cx):
        print(dy + 2)
    elif dy == 0 and not not_between(ay, by, cy):
        print(dx + 2)
    else:
        print(dx + dy)

