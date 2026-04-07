class Solution:
    # essentially find the pivot point?
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        # keep track of min?
        res = math.inf

        while left <= right:
            mid = (left + right) // 2

            res = min(res, nums[mid])

            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid -1

        return res 

            














            
# is our mid point in the left or rigt sorted?  

# find the inflection point, use binary search for that?
# that is the cur idx is greater than the next idx, how
# can this be done in log n?
# so binary search is basically searching for a given elem
# how is this differing? 