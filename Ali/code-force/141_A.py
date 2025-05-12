s1 = input().strip()
s2 = input().strip()
s3 = input().strip()
print("YES" if sorted(s1 + s2) == sorted(s3) else "NO")
