for _ in range(int(input())):
    n = int(input())
    s = input()
    solved = set()
    cnt = 0
    for i in s:
        if i not in solved:
            cnt += 2
            solved.add(i)
        else:
            cnt += 1
    print(cnt)
