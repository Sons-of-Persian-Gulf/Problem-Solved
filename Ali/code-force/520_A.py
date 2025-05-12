
n = int(input())
s = input()
if n < 26:
    print("NO")
else:
    chars = set(s.lower())
    print("YES" if len(chars) == 26 else "NO")
  