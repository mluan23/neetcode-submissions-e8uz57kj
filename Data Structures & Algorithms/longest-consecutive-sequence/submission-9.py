class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()

        for num in nums:
            num_set.add(num)

        starts = set()

        for num in num_set:
            if num-1 not in num_set:
                starts.add(num)
        longest = 1
        for num in starts:
            while num+1 in num_set:
                longest += 1
                num = num+1
        return longest
        