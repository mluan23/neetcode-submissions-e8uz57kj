class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n)
        if n == 1:
            return nums[0]
        if n== 2:
            return max(nums[0], nums[1])
        # the max is always gonna be the start house
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[n-1]
        
# keep track of the amt of money you can rob for each house
# from left ot right