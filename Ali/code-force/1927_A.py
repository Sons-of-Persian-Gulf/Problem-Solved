for _ in range(int(input())):
    n = int(input())
    s = input()
    first = True
    first_index = 0
    last_index = 0
    for i in range(n):
        if first and s[i] == "B":
            first = False
            first_index = i
        if s[i] == "B":
            last_index = i
    
    if first_index == last_index:
        print(1)
    else:
        print(abs(first_index - last_index) + 1)
        