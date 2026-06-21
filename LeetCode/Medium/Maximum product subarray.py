class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = float('-inf') 
        n = len(nums)
        pre = 1
        suff = 1
        for i in range(n):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            pre *= nums[i]
            suff *= nums[n-i-1]
            maxi = max(maxi, max(pre,suff))
        return maxi 
