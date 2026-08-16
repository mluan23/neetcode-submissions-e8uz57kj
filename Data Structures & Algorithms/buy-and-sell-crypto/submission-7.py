class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        max_profit = 0 
        # for stocks you wanna sell if your selling price is higher than your buying price
        # if your buying price is higher than your selling price then you just gotta advance the left 

        while right < len(prices):
            buy = prices[left]
            sell = prices[right]
            # we got a profit, the selling price is good
            if sell >= buy:
                right += 1
                max_profit = max(max_profit, sell-buy)
            else:
                left = right
                # right += 1
        return max_profit