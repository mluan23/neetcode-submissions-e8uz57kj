class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [1] * n
        postfix_prod = [1] * n

        for i in range(1,n):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1]
        
        for i in range(n-2,-1,-1):
            postfix_prod[i] = postfix_prod[i+1] * nums[i+1]
        
        res = [0] * n
        # print(prefix_prod, postfix_prod)
        for i in range(n):
            res[i] = postfix_prod[i] * prefix_prod[i]
        return res