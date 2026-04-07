class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starts = set()
        nums_set = set()
        max_count = 0
        for i in range(len(nums)):
            nums_set.add(nums[i])
        for i in range(len(nums)):
            if nums[i]-1 not in nums_set:
                starts.add(nums[i])
        for s in starts:
            cur_count = 1
            tmp = s
            while tmp + 1 in nums_set:
                cur_count += 1
                tmp += 1
            max_count = max(cur_count, max_count)
        return max_count