n = int(input())
coins = sorted(list(map(int, input().split())), reverse=True)
total = sum(coins)
my_share = 0
cnt = 0
for i in coins:
    if my_share <= total:
        my_share += i
        cnt += 1
        total -= i

print(cnt)
