n = int(input())
s = input().split()
is_hard = False

for i in s:
  if i == "1":
    is_hard = True
    break
print("HARD" if is_hard else "EASY")