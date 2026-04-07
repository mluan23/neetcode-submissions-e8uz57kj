class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        nums_set = set()
        starts = set()
        for i in range( len(nums)):
            nums_set.add(nums[i])
        for i in nums_set:
            if i-1 not in nums_set:
                starts.add(i)
        for i in starts:
            curr = i
            curr_len = 0
            while curr in nums_set:
                curr_len += 1
                curr += 1
            length = max(length, curr_len)
        return length
            

# so we don't care for repeat elems obv