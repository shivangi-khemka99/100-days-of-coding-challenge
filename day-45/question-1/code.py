class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # def helper(i, total):
        #     if i == len(nums):
        #         return total
        #     #Include nums[i] and not include nums[i]
        #     return helper(i+1, total ^ nums[i]) + helper(i+1, total)
        # return helper(0,0)
        res = 0
        for i in nums:
            res = res | i
        return res * pow(2, len(nums)-1) # res << len(nums)-1