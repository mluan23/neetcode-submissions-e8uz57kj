class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        n = len(prices)
        right = 1
        maximum = 0
        while right < n:
            sell_price = prices[right]
            buy_price = prices[left]
            maximum = max(maximum, sell_price - buy_price)
            if buy_price > sell_price:
                left += 1
            else:
                right += 1
        return maximum
            

