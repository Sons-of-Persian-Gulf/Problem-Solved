n = int(input())
state = input()
lock = input()
cnt = 0
for i in range(n):
    a = int(state[i])
    b = int(lock[i])
    # print(a, b)
    cnt += min(abs(a - b), min(a + 10 - b, 10 - a + b))
#     print(min(abs(a - b), min(10 - a + b, a + b)), end=" ")
# print()
print(cnt)
