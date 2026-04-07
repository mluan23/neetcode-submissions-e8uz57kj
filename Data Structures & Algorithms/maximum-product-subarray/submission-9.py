class Solution:
    # huh kadane's algorithm
    def maxProduct(self, nums: List[int]) -> int:
        # using the min because negative exist
        min_prod = nums[0]
        max_prod = nums[0]
        ret_max = nums[0]
        n = len(nums)
        for i in range(1,n):
            # your running total, or you take the new
            # subarray
            tmp = max_prod
            max_prod = max(max(min_prod * nums[i], nums[i]*max_prod), nums[i])
            #
            print(max_prod)
            min_prod = min(min(tmp* nums[i],min_prod* nums[i]), nums[i])
            print(min_prod)
            ret_max = max(max_prod, ret_max)

        return ret_max
            

# nvm misread q
# hmm so subarray need not be contiguous


# so essentially all you need is an even num 
# of negative nums
# in a given subarray
# but thats not exactly the intended way to look at it?

# dp[i] = max prod 
# essentially this problem is just finding 
# largest subarray with even num of negative nums
# and no 0s
