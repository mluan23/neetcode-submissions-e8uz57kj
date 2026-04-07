class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        seen = set()
        for i in range(len(nums)):
            target = -nums[i]
            l = 0
            r = i-1

            while l < r:
                if nums[l] + nums[r] == target:
                    ans = [nums[i],nums[l],nums[r]]
                    if tuple(ans) not in seen:
                        seen.add(tuple(ans))
                        res.append(ans)
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res