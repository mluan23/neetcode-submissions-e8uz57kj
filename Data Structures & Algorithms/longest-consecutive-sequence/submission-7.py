class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_as_set = set(nums)

        starts = set()

        if not nums:
            return 0

        for i in nums_as_set:
            if i - 1 not in nums_as_set:
                starts.add(i)
        maximum = 1
        for i in starts:
            count = 1
            num = i+1
            while num in nums_as_set:
                count += 1
                num += 1
            maximum = max(count, maximum)
        return maximum

        