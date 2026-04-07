class Solution:
    # idea's to find sort of where the pivot pt
    # is in the rotated arr
    # with the pivot point known, we know which way to go
    
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # we know we're in the right subarray
            elif nums[mid] >= nums[left]:
                # it must mean it's in the other subarray
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else: # nums[mid] <= nums[left]
            # so we're in the less subarray (left)
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

# [5 6 1 2 3 4] , target = 5
# [1 3]    targ = 3