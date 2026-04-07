class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # have a map to keep track of elements that appear x num times
        mappings = defaultdict(list)
        counts = {}
        res = []

        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
        
        for key in counts.keys():
            mappings[counts.get(key)].append(key)

        for i in range(len(nums), -1, -1):
            if i in mappings:
                arr = mappings.get(i)
                print(arr)
                for j in arr:
                    res.append(j)
                    k -= 1
                    if k == 0:
                        return res
        return res
                
            
            
