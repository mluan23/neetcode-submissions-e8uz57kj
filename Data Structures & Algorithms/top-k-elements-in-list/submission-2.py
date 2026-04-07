class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_mappings = dict()

        for i in range(len(nums)):
            n = nums[i]
            count_mappings[n] = count_mappings.get(n, 0) + 1

        buckets = dict()

        for i in range(1,len(nums)+1):
            buckets[i] = []
        
        for key in count_mappings:
            buckets[count_mappings.get(key)].append(key)
        res = []
        for i in range(len(nums), 0, -1):
            for val in buckets.get(i):
                if len(res) == k:
                    return res
                res.append(val)
        return res
