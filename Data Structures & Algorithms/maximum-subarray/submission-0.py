class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -sys.maxsize - 1
        dp = [0] * len(nums)
        dp[0] = nums[0]
        # largest possible sum ending at idx i?
        # dp[i] will be the largest sum at idx i
        for i in range (1, len(nums)):
            dp[i] = nums[i]
            if dp[i-1] >= 0:
                dp[i] += dp[i-1]
        return max(dp)
        

