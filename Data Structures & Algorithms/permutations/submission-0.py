class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        curr = []
        seen = [False] * len(nums)
        
        def backtrack(nums, seen, curr, res):
            # so for each level, make every possible choice;
            # how do we do that?
            # so if same len, then gotta add
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if seen[i]:
                    continue
                curr.append(nums[i])
                seen[i] = True
                backtrack(nums, seen, curr, res)
                curr.pop()
                seen[i] = False
        backtrack(nums, seen, curr, res)
        return res
            # so your choices should be to add any of the other
            # elements right?
            
            
                
            
            
            
            