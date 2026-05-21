class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        n = len(nums)
        right =n-1
        while left <= right:
            # the target does not tell us anything about the 
            # the location we are in for the sorted portion
            # all that matters is the left in relation to mid and right

            mid = (left + right) // 2
            # this essentially means that we are in the 
            # sorted way
            if nums[mid] == target:
                return mid
            # i mean this is all that matters to see where we are in the sorted part
            if nums[left] <= nums[mid]:
                # proceed as usual
                # if mid > target, then gotta decrement mid
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                # if mid pt is less than target
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1