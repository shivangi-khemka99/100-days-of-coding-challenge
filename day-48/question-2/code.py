class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        diff_bit = 1
        while not (xor & diff_bit):
            diff_bit = diff_bit << 1
        a,b = 0,0
        for num in nums:
            if diff_bit & num:
                a ^= num
            else:
                b ^= num
        return [a,b]