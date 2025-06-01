n = int(input())

dp = [0 for _ in range(25)]
dp[0] = 1
dp[1] = 0
dp[2] = 3
dp[3] = 0

if n % 2 == 1:
    # if n is odd there is always a gap:
    print(0)


elif n <= 3:
    print(dp[n] * 2)
else:
    for i in range(4, n + 1):
        dp[i] = 4 * dp[i - 2] - dp[i - 4]

    print(dp[n] * 2)