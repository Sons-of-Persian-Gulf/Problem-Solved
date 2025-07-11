s = input()
x1 = s[0].isupper()
x2 = all(i.isupper() for i in s[1:])

if x1 and x2:
    print(s.lower())
elif not x1 and x2:
    print(s[0].upper() + s[1:].lower())
else:
    print(s)