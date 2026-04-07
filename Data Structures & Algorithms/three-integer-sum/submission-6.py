class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums = sorted(nums)

        seen = set()

        for i in range(len(nums)): 
            # cause i should always be greater
            target = -1*nums[i]
            j = 0
            k = i - 1

            while j < k:
                if nums[j] + nums[k] == target:
                    ans = [nums[i],nums[j],nums[k]]
                    if tuple(ans) not in seen:
                        seen.add(tuple(ans))
                        res.append(ans)
                    j += 1
                    k -= 1
                else:
                    if nums[j] + nums[k] > target:
                        k -= 1
                    else:
                        j += 1
        return res
                