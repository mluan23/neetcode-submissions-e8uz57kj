class Solution:
    # why do we need res??
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        if nums[-1] > nums[0]:
            return nums[0]
        left = 0
        right = len(nums)-1
        res = nums[0]
        while left <= right:
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[left] < nums[right]:
                return min(res, nums[left])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return res
            
# is our mid point in the left or rigt sorted?  

# find the inflection point, use binary search for that?
# that is the cur idx is greater than the next idx, how
# can this be done in log n?
# so binary search is basically searching for a given elem
# how is this differing? 