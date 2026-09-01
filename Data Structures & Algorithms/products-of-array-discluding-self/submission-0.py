class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix products
        n = len(nums)
        prefix_prod = [1] * n
        prefix_prod[0] = nums[0]
        for i in range(1,n):
            prefix_prod[i] = nums[i] * prefix_prod[i-1]
        suffix_prod = [1] * n
        suffix_prod[-1] = nums[-1]
        for i in range(n-2, -1,-1):
            suffix_prod[i] = nums[i] * suffix_prod[i+1]
        res = [1] * n
        res[0] = suffix_prod[1]
        res[-1] = prefix_prod[-2]
        for i in range(1, n-1):
            res[i] = prefix_prod[i-1] * suffix_prod[i+1]
        
        return res