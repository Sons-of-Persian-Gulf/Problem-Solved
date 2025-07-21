for _ in range(int(input())):
    s = input()
    if s.startswith("10"):
        exponent_part = s[2:]
        if exponent_part not in {"0", "1"} and exponent_part.isdigit() and not exponent_part.startswith("0"):
            print("YES")
            continue
    print("NO")
