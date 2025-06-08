for _ in range(int(input())):
    n = int(input())
    s = input()
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
        continue
    elif (s[0] == "1" and s[-1] == "0") or (s[0] == "0" and s[-1] == "1"):
        cnt = 0
        i = 0
        j = n -1
        while i < n // 2:
            if (s[i] == "1" and s[j] == "0") or (s[i] == "0" and s[j] == "1"):
                cnt += 2
                i += 1
                j -= 1
            else:
                break
        print(n - cnt)
    else:
        print(n)