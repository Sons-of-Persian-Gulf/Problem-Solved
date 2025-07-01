for _ in range(int(input())):
    s = input().strip()  # strip spaces/newlines
    target = "acpc"
    idx = 0
    for ch in s:
        if idx < len(target) and ch == target[idx]:
            idx += 1
            if idx == len(target):
                break
    print("YES" if idx == len(target) else "NO")
