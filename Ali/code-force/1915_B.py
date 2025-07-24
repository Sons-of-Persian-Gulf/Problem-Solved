# for _ in range(int(input())):
#     arr = []
#     for _ in range(3):
#         arr.append(list(input()))
#     for i in range(3):
#         if "?" in arr[i]:
#             if "A" not in arr[i]:
#                 print("A")
#             elif "B" not in arr[i]:
#                 print("B")
#             else:
#                 print("C")
t = int(input())

for _ in range(t):
    xor_all = 0
    full_xor = ord('A') ^ ord('B') ^ ord('C')  # A ^ B ^ C = 65 ^ 66 ^ 67 = 64
    for _ in range(3):
        row = input().strip()
        for ch in row:
            if ch != '?':
                xor_all ^= ord(ch)
    missing = xor_all ^ full_xor
    print(chr(missing))
