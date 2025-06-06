class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * n
        for i in range(n):
            if i in (0, 1):
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[n - 1], dp[n - 2])


s = Solution()
print(s.minCostClimbingStairs([10,15,20]))
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))