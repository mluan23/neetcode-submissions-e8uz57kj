class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        # assume we cannot make any amounts to start

        dp = [-1] * (amount+1)
        dp[0] = 0
        
        # find the min num of coins for each amount,
        # up to desired amount
        for i in range(1,amount+1):
            for coin in coins:
                if i - coin >= 0:
                    # this means we can make the amt
                    if dp[i - coin] != -1:
                        test = dp[i-coin] + 1
                        if dp[i] == -1:
                            dp[i] = dp[i-coin] + 1
                        # current or the new coin?
                        else:
                            dp[i] = min(dp[i], test)
        return dp[-1]

# dp[i] = fewest num coins to make amt i
# [1,5,10]
# 1 = 1
# 2 = 1 1
# 3 = 1 1 1
# 4 = 