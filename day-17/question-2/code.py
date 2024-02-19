class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0,len(nums)-1
        num = []
        while l<=r:
            opL = nums[l]**2
            opR = nums[r]**2
            if  opL > opR:
                num.append(opL)
                l+=1
            else:
                num.append(opR)
                r-=1
        return num[::-1]
        #Time complexty: O(N) ; Space complexity: O(N)