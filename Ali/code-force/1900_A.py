t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    flag = True
    count = 0

    for i in range(n):
        if s[i] == '.':
            count += 1
        if i > 0 and i < n - 1:
            if s[i - 1] == '.' and s[i] == '.' and s[i + 1] == '.':
                print(2)
                flag = False
                break

    if flag:
        print(count)
