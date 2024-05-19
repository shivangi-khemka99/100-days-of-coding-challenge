class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        delta = [(n^k) - n for n in nums]
        delta.sort(reverse=True)
        res = sum(nums)

        for i in range(0,len(nums),2):
            if i!=len(nums)-1:
                if delta[i] + delta[i+1] > 0 :
                    res+= delta[i] + delta[i+1] 
        return res