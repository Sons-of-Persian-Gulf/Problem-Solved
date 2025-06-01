n = int(input())

for _ in range(n):
    cnt = 0
    for i in range (1, 11):
        x = input()
        for j in range(1, 11):
            if x[j - 1] == "X":
                if 5 <= i <= 6 and 5 <= j <= 6:
                    cnt += 5
                elif 4 <= i <= 7 and 4 <= j <= 7:
                    cnt += 4
                elif 3 <= i <= 8 and 3 <= j <= 8:
                    cnt += 3
                elif 2 <= i <= 9 and 2 <= j <= 9:
                    cnt += 2
                else:
                    cnt += 1
    print(cnt)






