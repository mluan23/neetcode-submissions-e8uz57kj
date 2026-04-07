class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if (nums[i] > nums[j]):
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
# dp[i] will be the 
# 9, 1, 4, 2, 3, 4, 7
# 1, 1, 2, 2, 3, 3, 4