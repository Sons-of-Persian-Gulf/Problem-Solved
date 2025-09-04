import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        c0 = s.count('0')
        c1 = len(s) - c0
        if c0 == c1:
            print(c0 - 1)
        else:
            print(min(c0, c1))

if __name__ == "__main__":
    solve()
