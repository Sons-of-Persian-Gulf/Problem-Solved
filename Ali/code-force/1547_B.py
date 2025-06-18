from collections import deque
for _ in range(int(input())):
    s = deque(input())
    ok = True
    for i in range(len(s), 0, - 1):
        c = chr(i + 96)
        if c == s[-1]:
            s.pop()
        elif c == s[0]:
            s.popleft()
        else:
            ok = False
            break
    print("YES" if ok else "NO")
