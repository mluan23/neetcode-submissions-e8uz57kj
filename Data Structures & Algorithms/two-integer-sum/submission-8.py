class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevs = dict()

        for i in range(len(nums)):
            curr = nums[i]

            if target - curr in prevs:
                return [prevs.get(target-curr), i]
            prevs[curr] = i
        return []