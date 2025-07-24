t = int(input())
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    oranges = list(map(int, input().split()))

    mn_c = min(candies)
    mn_o = min(oranges)
    moves = 0

    for i in range(n):
        diff_c = candies[i] - mn_c
        diff_o = oranges[i] - mn_o
        moves += max(diff_c, diff_o)

    print(moves)
