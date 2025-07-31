import re
for _ in range(int(input())):
    n = int(input())
    s = input()
    pattern = r'^m+e+o+w+$'

    if re.fullmatch(pattern, s.lower()):
        print("YES")
    else:
        print("NO")