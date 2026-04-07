class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0

        dp = {}

        if len(nums) == 0:
            return 0
        unique = set(nums)
        longest = 1
        for u in unique:
            count = 1
            if u - 1 not in unique:
                while u + 1 in unique:
                    u = u + 1
                    count += 1
                    longest = max(count, longest)
        return longest
            

# so we don't care for repeat elems obv