r1, c1, r2, c2 = map(int, input().split())

def rook(r1, c1, r2, c2):
    return 1 if r1 == r2 or c1 == c2 else 2

def color(r, c):
    return "B" if (r + c) % 2 == 0 else "W"

def bishop(r1, c1, r2, c2):
    if color(r1, c1) != color(r2, c2):
        return 0
    elif abs(r1 - r2) == abs(c1 - c2):
        return 1
    else:
        return 2

def king(r1, c1, r2, c2):
    return max(abs(r1 - r2), abs(c1 - c2))

print(rook(r1, c1, r2, c2), bishop(r1, c1, r2, c2), king(r1, c1, r2, c2))
