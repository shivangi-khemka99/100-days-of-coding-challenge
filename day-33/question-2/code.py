class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                digits[i - 1] -= 1
                digits[i:] = [9] * (len(digits) - i)
        return int(''.join(map(str, digits)))