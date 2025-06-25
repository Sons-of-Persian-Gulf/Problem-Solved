pattern = "Yes" * 20
for _ in range(int(input())):
    s = input()
    print("Yes" if s in pattern else "NO")
