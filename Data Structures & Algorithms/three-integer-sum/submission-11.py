class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorts in ascending
        nums.sort()
        n = len(nums)
        # but whats our target?
        res = []
        for i in range(n-2):
            # we use 2 ptrs
            # right must be capped at i, because target must 
            # be less
            # target will just be i itself then
            # because you obv are gonna need 
            # nums[i] = -nums[j] - nums[k]
            # same for all rly

            # ok then ig we need to change it a lil

            # because nums[i] is the smallest
            if nums[i] > 0:
                break
            # skipping the sorta anchor element, avoid dupes
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            # not <= because they must be distinct indices
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total == 0:
                    res.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                    
                    # and we still need to avoid dupes
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    # need to make bigger
                    left += 1
                else:
                    right -= 1
        return res



