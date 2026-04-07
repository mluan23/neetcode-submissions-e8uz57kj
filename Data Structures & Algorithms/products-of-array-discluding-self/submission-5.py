class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # take everything to the left of this
        left = [1] * n
        # take everything to the right of this
        right = [1] * n

        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        # [1,2,4,6]
        # L [1,1,2,8]
        # R [48, 24, 6, 1]
        # comb [48, 24, 12, 8]
        res = []
        for i in range(n):
            res.append(left[i] * right[i])
        return res