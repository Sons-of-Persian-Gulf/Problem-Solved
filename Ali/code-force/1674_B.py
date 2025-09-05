dict = {}
chars = "abcdefghijklmnopqrstuvwxyz"
index = 1
for i in chars:
    for j in chars:
        if i == j:
            continue
        dict[f"{i}{j}"] = index
        index += 1

for _ in range(int(input())):
    print(dict[input()])