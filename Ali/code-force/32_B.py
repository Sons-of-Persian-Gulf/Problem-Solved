# s = input()
# ans = ""
# flag = False
# stack = []
# for i in range(0, len(s)):
#     if s[i] == "-" and stack and stack[-1] == "-":
#         ans += "2"
#         stack.pop()
#     elif s[i] == "." and stack and stack[-1] == "-":
#         ans += "1"
#         stack.pop()
#     elif s[i] == ".":
#         ans += "0"
#     else:
#         stack.append(s[i])
# print(ans)


s = input()
i = 0
res = ""

while i < len(s):
    if s[i] == '.':
        res += '0'
        i += 1
    elif s[i] == '-':
        if s[i + 1] == '.':
            res += '1'
        else:  # s[i + 1] == '-'
            res += '2'
        i += 2  # Skip the next character

print(res)
