n = input()
def lucky_number(number):
    lucky = True
    for char in number:
        if char != "4" and char != "7":
            lucky = False
            break
    return lucky


if lucky_number(n):
    print("YES")
    exit()
arr = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
for i in arr:
    if int(n) % i == 0:
        print("YES")
        exit()

print("NO")
