class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        n = len(nums)
        right =n
        while left <= right:
            # the target does not tell us anything about the 
            # the location we are in for the sorted portion
            # all that matters is the left in relation to mid and right

            mid = (left + right) // 2
            # this essentially means that we are in the 
            # sorted way
            if nums[mid] == target:
                return mid
            if left <= mid:
                # proceed as usual
                if left <= target < mid:
                    left = mid +1
                else:
                    right = mid - 1
            else:
                if mid < target <= right:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1