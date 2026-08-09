class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # or heap works too
        freqs = dict()

        for n in nums:
            freqs[n] = freqs.get(n,0) + 1
        
        buckets = dict()
        for i in range(0,len(nums)+1):
            buckets[i] = []

        for num,val in freqs.items():
            buckets[val].append(num)

        res = []
        for i in range(len(nums), -1, -1):
            bucket = buckets[i]
            for num in bucket:
                res.append(num)
                k -= 1
                if k == 0:
                    return res
        return []