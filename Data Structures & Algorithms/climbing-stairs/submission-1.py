class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        if n == 1:
            return 1
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# 1
# 11, 2
# 111, 21, 12
# 1111, 211, 121, 112, 22
# 11111, 2111, 1211, 1121, 221, 122, 1112
