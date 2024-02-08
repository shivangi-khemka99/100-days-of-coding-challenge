class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sumArr = []
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            self.sumArr.append(summ)

    def sumRange(self, left: int, right: int) -> int:
        return self.sumArr[right] - ( 0 if left == 0 else self.sumArr[left-1])