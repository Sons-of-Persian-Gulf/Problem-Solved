# arr = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}


for _ in range(int(input())):
    c, y  = list(input())
    x = ord(c) - 96  # Convert column letter to number (1-8)
    y = int(y)
    for i in range(1, 9):
        if i != y:
            print(f"{c}{i}")  # Same column, different row
        if i != x:
            print(f"{chr(i + 96)}{y}")  # Same row, different column