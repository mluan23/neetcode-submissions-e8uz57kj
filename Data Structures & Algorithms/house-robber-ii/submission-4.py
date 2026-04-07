class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp1 = [0] * (n-1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[1], nums[0])

        dp = [0] * (n)
        dp[1] = nums[1]
        dp[2] = max(nums[1], nums[2])

        for i in range(2, n-1):
            dp1[i] = max(nums[i] + dp1[i-2], dp1[i-1])
        for i in range(3, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return max(dp[-1], dp1[-1])

# 0-200 1-200 2

# dp[i] = maximum that you can rob at index i
# i can always rob house 0 right?
# start anywhere, it should be same outcome
# it's eiher you rob this house, or rob the other two,
# but we cant rob first and last
# so now we can't just use dp[i-2]
# so you literally cannot have both, so you're supposed
# to just one two arrays then, strange