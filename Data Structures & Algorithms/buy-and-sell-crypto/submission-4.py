class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        l = 0
        r = 0
        while l <= r and r < len(prices):
            profit = prices[r] - prices[l]
            maximum = max(profit, maximum)
            if prices[l] > prices[r]:
                l += 1
            else:
                r += 1
        return maximum
            

