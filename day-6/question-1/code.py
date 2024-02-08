class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total, leftSum = sum(nums), 0
        for i in range(len(nums)):
            if i == 0:
                leftSum = 0
            else:
                leftSum += nums[i-1]
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
        return -1