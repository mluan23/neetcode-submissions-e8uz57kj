class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # nums.sort()
        # for i in range(len(nums)):
        self.traverse(res, 0, target, [], nums, 0)
        return list(res)

    def traverse(self, res, cur_sum, target, cur_nums, nums, idx):
        if idx >= len(nums):
            return
        if idx < 0:
            return
        if cur_sum > target:
            return
        if cur_sum == target:
            cur_nums.sort()
            if cur_nums not in res:
                res.append(cur_nums)
            return
        for i in range(len(nums)):
            self.traverse(res, cur_sum + nums[i], target, cur_nums + [nums[i]], nums, i)

        # self.traverse(res, cur_sum + nums[idx], target, cur_nums + [nums[idx]], nums, idx)
        # if idx - 1 > 0:
        #     self.traverse(res, cur_sum + nums[idx - 1], target, cur_nums + [nums[idx - 1]], nums, idx - 1)
        # if idx + 1 < len(nums):
        #     self.traverse(res, cur_sum + nums[idx + 1], target, cur_nums + [nums[idx + 1]], nums, idx + 1)

        


        