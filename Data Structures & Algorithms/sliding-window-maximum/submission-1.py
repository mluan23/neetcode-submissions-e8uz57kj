class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # window is size k
        res = [-1*math.inf] * (len(nums)-k+1)

        for i in range(len(nums)-k+1):
            for j in range(k):
                res[i] = max(res[i], nums[i+j])
        return res