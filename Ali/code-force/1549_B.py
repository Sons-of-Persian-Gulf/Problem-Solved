for _ in range(int(input())):
    n = int(input())
    enemy_pawns = list(input()[::1])
    self_pawns = list(input()[::1])
    cnt = 0

    pos = [-1, 1]

    def is_bound(x):
        return 0 <= x < n


    for i in range(n):
        if self_pawns[i] == "1":
            if enemy_pawns[i] == "0":
                cnt += 1
            else:
                if is_bound(i - 1) and enemy_pawns[i - 1] == "1":
                    cnt += 1
                    enemy_pawns[i - 1] = "0"
                elif is_bound(i + 1) and enemy_pawns[i + 1] == "1":
                    cnt += 1
                    enemy_pawns[i + 1] = "0"
    print(cnt)


