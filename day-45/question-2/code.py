class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def helper(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 
            #Include nums[i]
            subset.append(nums[i])
            helper(i+1)
            #Don't include nums[i]
            subset.pop()
            helper(i+1)
        helper(0)
        return res