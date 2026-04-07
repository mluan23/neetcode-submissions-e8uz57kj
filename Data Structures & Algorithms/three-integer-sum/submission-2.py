class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[i] + nums[l] + nums[r] == 0 and l < r:
                        l += 1
        return res
            


# -nums[i] == nums[j] + nums[k]
# so effectively -nums[i] = target and nums[j]
# and nums[k] are our two values we care about
# now the difference between this and two-sum is
# that we want all triplets, and that's what makes this 
# to be O(n^2). if just one triplet, i believe that 
# could be in just O(n)?

# the brute force way is to do triple loop. how can we 
# kind of use that idea and improve it? 