# Same Size?
a = input()
b = input()
arr = ["AB", "BC", "CD", "DE", "EA",]
arr2 = ["AD", "AC", "BE", "BD", "CE"]
x1 = ((a in arr) or (a[::-1] in arr)) and ((b in arr) or (b[::-1] in arr))
x2 = ((a in arr2) or (a[::-1] in arr2)) and ((b in arr2) or (b[::-1] in arr2))
print("Yes" if x1 or x2 else "No")
