class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set()
        starts = set()
        # so we might want to sort this, but cant cause O(n)

        # actually the only thing we care about is the start of
        # a sequence
        res = 0
        for i in nums:
            a.add(i)
            if i-1 not in starts:
                starts.add(i)
        
        for i in starts:
            counts = 1
            n = i
            while n+1 in a:
                counts += 1
                n += 1
            res = max(res, counts)
        return res

