import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        logValue = log10(n) / log10(3)
        return logValue.is_integer()