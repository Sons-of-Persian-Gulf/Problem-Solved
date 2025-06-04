n = int(input())

for _ in range(n):
    x = int(input())

    if x == 1 or (x + 1) % 3 == 0 or (x - 1) % 3 == 0:
        print("First")
    else:
        print("Second")



