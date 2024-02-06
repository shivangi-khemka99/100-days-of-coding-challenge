class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if (val not in nums):
            return len(nums)
        x,y=0,len(nums)-1
        while (x<y):
            if nums[x] == val and nums[y] != val:
                nums[x],nums[y] = nums[y],nums[x]
                x+=1
            elif nums[x] != val:
                x+=1
            elif nums[y] == val:
                y-=1
        return y
        #O(logN)