n, x = map(int, input().split())
distress = 0
for _ in range(n):
    op, quantity = input().split()
    quantity = int(quantity)
    if op == "+":
        x += quantity
    else:
        if quantity <= x:
            x -= quantity
        else:
            distress += 1
print(x, distress)